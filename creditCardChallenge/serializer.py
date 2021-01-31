from rest_framework import serializers
from creditCardChallenge.models import CreditCard

class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = '__all__'
    
    def viewRepresentation(self,instance):
        representation = super(CreditCardSerializer, self).viewRepresentation(instance)

        return representation