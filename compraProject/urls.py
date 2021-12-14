from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from compraApp import views
urlpatterns = [
    path('transaction/<int:user>/', views.TransactionCreateView.as_view()),
    path('transaction/<int:user>/<int:pk>/', views.TransactionDetailView.as_view()),
    path('transaction/list/<int:user>/', views.TransactionListView.as_view()),
    path('transaction/remove/<int:user>/<int:pk>/', views.TransactionDeleteView.as_view()),
    path('transaction/update/<int:user>/<int:pk>/', views.TransactionUpdateView.as_view()),
    path('creditCard/<int:user>/', views.CreditCardCreateView.as_view()),
    path('creditCard/list/<int:user>/', views.CardListView.as_view()),
    path('creditCard/remove/<int:user>/<int:pk>/', views.CreditCardDeleteView.as_view()),
    path('creditCard/update/<int:user>/<int:pk>/', views.CreditCardUpdateView.as_view()),
]
