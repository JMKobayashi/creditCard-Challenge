from django.urls import path
from . import views

urlpatterns = [
    path('list-credit-card/', views.creditCardsView.as_view(), name='credit-cards-list'),
    path('credit-card-detail/<int:pk>',views.creditCardDetail.as_view(), name='credit-card-detail')
]