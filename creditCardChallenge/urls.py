from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('credit-card/', views.creditCardsView.as_view(), name='credit-card'),
    path('token/', obtain_auth_token, name='api-auth-token')
]