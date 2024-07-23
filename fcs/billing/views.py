from django.shortcuts import render

# Create your views here.


def billing_home(request):
    return render(request, template_name='billing/billing_home.html')
