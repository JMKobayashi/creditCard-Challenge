from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'listCreditCard', views.creditCardsView.as_view(), name='creditCard')
]