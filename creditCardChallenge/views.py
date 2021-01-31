from rest_framework import viewsets
from creditCardChallenge.models import creditCard
from serializer import CreditCardSerializer

class creditCardsViewSet(viewsets.ModelViewSet):

    queryset = creditCard.objects.all()
    serializer_class = CreditCardSerializer
