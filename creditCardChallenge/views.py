from rest_framework.parsers import JSONParser
from restframework import status
from rest_framework.view import APIview

from creditCardChallenge.models import CreditCard
from creditCardChallenge.serializer import CreditCardSerializer

from django.http.response import JsonResponse

class creditCardsViewSet(APIview):

    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
