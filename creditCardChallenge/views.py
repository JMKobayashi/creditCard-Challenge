from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.view import APIview

from creditCardChallenge.models import CreditCard
from creditCardChallenge.serializer import CreditCardSerializer

from django.http.response import JsonResponse

class creditCardsViewSet(APIview):

    def get(self,request):
        credit_card_list = CreditCard.objects.all()

        credit_card_id = 
