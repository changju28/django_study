# 앱에서 어떤 기능을 할지에 대한 메인 로직을 담당하는 파일
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'foods/index.html')