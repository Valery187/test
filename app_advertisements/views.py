from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def lessonFour(request):
    return HttpResponse('Домашка по 4 занятию')


def top_sellers(request):
    return render(request,'top-sellers.html')