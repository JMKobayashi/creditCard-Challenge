from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView

from creditCardChallenge.models import CreditCard
from creditCardChallenge.serializer import CreditCardSerializer

from django.http.response import JsonResponse

class creditCardsViewSet(APIView):

    def get(self,request):
        credit_card_list = CreditCard.objects.all()
        
        # Verifying if ID is in the parameters passed in GET REQUEST
        credit_card_id = request.query_params.get('id',None)
        
        # if a parameter is passed filter results by parameter
        if credit_card_id is not None:
            credit_card_list = credit_card_list.filter(id=credit_card_id)
        
        serializer_result = CreditCardSerializer
        return serializer_result


