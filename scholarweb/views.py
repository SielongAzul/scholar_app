from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#This is where to put all of dynamic pages.

def index(request):
    return render(request, 'scholarweb/index.html')

def test(request):
    return HttpResponse('Not Index')
