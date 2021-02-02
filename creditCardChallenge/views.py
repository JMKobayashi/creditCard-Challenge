from rest_framework.parsers import JSONParser
from rest_framework import status, generics
from rest_framework.views import APIView

from creditCardChallenge.models import CreditCard
from creditCardChallenge.serializer import CreditCardSerializer

from django.http.response import JsonResponse

class creditCardsView(APIView):

    def get(self,request):
        credit_card_list = CreditCard.objects.all()

        credit_card_id = request.query_params.get('id',None)

        if credit_card_id is not None:
            credit_card = CreditCard.objects.filter(id=int(credit_card_id))
        else:
            credit_card = credit_card_list

        serializer_result = CreditCardSerializer(credit_card, many = True)
        return JsonResponse(serializer_result.data + [credit_card_id],safe=False,)

    def post(self,request):
        
        json_request = JSONParser().parse(request)
        dataSerializer = CreditCardSerializer(data=data)

        dataSerializer.save()
        return JsonResponse(dataSerializer.data, status = HTTP_201_CREATED)
