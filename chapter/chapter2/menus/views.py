from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def restuarant(request):
    return HttpResponse('<h1>코스토랑 오픈!</h1>')