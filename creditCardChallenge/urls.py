from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list-credit-card/', views.creditCardsView.as_view(), name='credit-cards-list'),
    url(r'^credit-card-detail/<int:pk>',views.creditCardDetail.as_view(), name='credit-card-detail')
]