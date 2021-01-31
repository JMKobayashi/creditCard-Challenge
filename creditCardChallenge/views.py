from rest_framework import viewsets
from escola.models import creditCard
from serializer import CreditCardSerializer

class creditCardsViewSet(viewsets.ModelViewSet):

    queryset = Aluno.objects.all()
    serializer_class = CreditCardSerializer
