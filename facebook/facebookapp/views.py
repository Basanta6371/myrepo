from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    x="welcome to nth django session"
    return HttpResponse(x)

def contact(request):
    x="our contact number is 6371917736"
    return HttpResponse(x)

def services(request):
    x="we provide all services"
    return HttpResponse(x)
def feedback(request):
    x="we have good feed back"
    return HttpResponse(x)


