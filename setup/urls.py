from django.contrib import admin
from django.urls import path,include
from creditCardChallenge.views import creditCardsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('listCreditCard',creditCardsViewSet, basename='creditCard')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
