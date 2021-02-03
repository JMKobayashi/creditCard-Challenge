from django.contrib import admin
from creditCardChallenge.models import CreditCardModel

class CreditCards(admin.ModelAdmin):
    list_display = ('id','exp_date','holder','number','cvv')
    list_display_links = ('id','number')
    search_fields = ('id','number')
    list_per_page = 10

admin.site.register(CreditCardModel,CreditCards)
