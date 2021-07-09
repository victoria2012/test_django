from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>안녕하세요. 주창석입니다.</h1>')