from rest_framework import serializers
from creditCardChallenge.models import CreditCardModel
from .function import creditCardFunction

from datetime import datetime
import calendar
import re

from creditcard import CreditCard

class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCardModel
        fields = '__all__'
    
    # Validating parameters field to save in the database

    def validate_exp_date(self,value):
        # validating the date
        value = value.replace("-","/")
        try:
            if len(value) == 10:
                date = datetime.strptime(value, "%d/%m/%Y")
                full_year = True
            elif len(value) == 8:
                date = datetime.strptime(value,"%d/%m/%y")
                full_year = False
            elif len(value) == 7:
                date = datetime.strptime(value,"%m/%Y")
                full_year = True
            else:
                date = datetime.strptime(value,"%m/%y")
                full_year = False
        except ValueError:
            raise serializers.ValidationError("exp_date is invalid.")

        last_day_month = calendar.monthrange(date.year,date.month)[1]
        if date.month < 10:
            month = "0" + str(date.month)
        
        if (full_year):
            year = date.year()
        else:
            year = date.strftime("%Y")

        exp_date = str("{}-{}-{}".format(year,date.month,last_day_month))
        exp_datetime = datetime.strptime(exp_date, "%Y-%m-%d")
        today = datetime.today()
        if today > exp_datetime:
            raise serializers.ValidationError("exp_date is in the past!!")

        return exp_date

    def validate_holder(self, value):
        if (len(value)<3):
            raise serializers.ValidationError("Holder has less than 3 characters")
        
        return value
    
    def validate_number(self,value):
        validated_cc = CreditCard(value)

        if not validated_cc.is_valid():
            raise serializers.ValidationError("Credit Card is not valid")
        
        else:
            try:
                self.initial_data['brand'] = validated_cc.get_brand()
            except ValueError:
                raise serializers.ValidationError("Brand was'nt found for this card")

        encrypted_number = creditCardFunction.encrypt(value)
        return encrypted_number

    def validate_cvv(self,value):
        if len(value) > 4:
            raise serializers.ValidationError("cvv has more than 4 digits")
        
        if len(value) < 3:
            raise serializers.ValidationError("cvv has less tha 3 digits")

        return value

    def to_representation(self,instance):
        representation = super(CreditCardSerializer, self).to_representation(instance)
        creditcard_number = representation["number"]
        representation["number"] = creditCardFunction.decrypt(creditcard_number)
        return representation
