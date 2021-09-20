from django.shortcuts import render
# from registration.models import __model-name__

# Create your views here.


def registration(request):
    return render(request, 'registration/register.html')
