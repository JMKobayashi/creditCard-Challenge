from django.contrib import admin
from django.urls import path,include
from creditCardChallenge.views import creditCardsView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('listCreditCard',creditCardsView.as_view(), basename='creditCard')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
