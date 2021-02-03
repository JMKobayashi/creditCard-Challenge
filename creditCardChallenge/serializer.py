from rest_framework import serializers
from creditCardChallenge.models import CreditCardModel

from datetime import datetime

class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
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

        return date

    def validate_holder(self, value):
        if (len(value)<2):
            raise serializers.ValidationError("Holder has less than 3 characters")
        
        return value
    
    def validate_number(self,value):
        return value

    def validate_cvv(self,value):
        if len(value) > 4:
            raise serializers.ValidationError("cvv has more than 4 digits")
        
        if len(value) < 3:
            raise serializers.ValidationError("cvv has less tha 3 digits")

        return value

    def viewRepresentation(self,instance):
        representation = super(CreditCardSerializer, self).viewRepresentation(instance)

        return representation
