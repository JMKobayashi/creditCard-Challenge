from rest_framework import viewsets
from creditCardChallenge.models import CreditCard
from creditCardChallenge.serializer import CreditCardSerializer

class creditCardsViewSet(viewsets.ModelViewSet):

    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
