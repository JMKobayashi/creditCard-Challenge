from rest_framework.parsers import JSONParser
from rest_framework import status, generics
from rest_framework.views import APIView

from creditCardChallenge.models import CreditCardModel
from creditCardChallenge.serializer import CreditCardSerializer

from django.http.response import JsonResponse

class creditCardsView(APIView):

    def get(self,request):
        credit_card_list = CreditCardModel.objects.all()

        credit_card_id = request.query_params.get('id',None)

        if credit_card_id is not None:
            credit_card = CreditCardModel.objects.filter(id=int(credit_card_id))
        else:
            credit_card = credit_card_list

        serializer_result = CreditCardSerializer(credit_card, many = True)
        return JsonResponse(serializer_result.data,safe=False)

    def post(self,request):
        
        json_request = JSONParser().parse(request)
        dataSerializer = CreditCardSerializer(data=json_request)

        if dataSerializer.is_valid(raise_exception=True):

            dataSerializer.save()
            return JsonResponse(dataSerializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(dataSerializer.data,status=status.HTTP_400_BAD_REQUEST)
