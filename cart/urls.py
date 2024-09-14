from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='detail'),
]