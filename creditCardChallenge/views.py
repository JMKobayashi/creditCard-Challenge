from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView, generics

from creditCardChallenge.models import CreditCard
from creditCardChallenge.serializer import CreditCardSerializer,CreditCardDetailSerializer

from django.http.response import JsonResponse

class creditCardsView(APIView):

    def get(self,request):
        credit_card_list = CreditCard.objects.all()

        serializer_result = CreditCardSerializer(credit_card_list, many = True)
        return JsonResponse(serializer_result.data,safe=False,)


class creditCardDetail(generics.ListAPIView):
    def get_querySet(self):
        querySet = Matriculas.objects.filter(id=self.kwarg['pk'])
        return querySet