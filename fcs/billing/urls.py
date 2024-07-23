from django.urls import path
from .views import billing_home

app_name = 'billing'

urlpatterns = [
    path('', billing_home, name='billing_home'),
    ]
