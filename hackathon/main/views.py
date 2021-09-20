from django.shortcuts import render
# from main.models import __model-name__

# Create your views here.


def home(request):
    return render(request, 'main/landing.html')