from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog


# Create your views here.

def lists(request):
    return render(request,'index.html')
def create(request):
    return HttpResponse('I love My django experience')
def details(request):
    pass
def update(request):
    pass

    
    
