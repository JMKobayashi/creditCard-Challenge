from rest_framework import serializers
from creditCardChallenge.models import CreditCard

from datetime import datetime

class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = '__all__'
    
    # Validating parameters field to save in the database

    def exp_date_validate(self,value):
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




    def viewRepresentation(self,instance):
        representation = super(CreditCardSerializer, self).viewRepresentation(instance)

        return representation
