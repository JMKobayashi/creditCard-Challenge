from django.urls import path
from . import views

urlpatterns = [
    path('credit-card/', views.creditCardsView.as_view(), name='credit-card'),
]