from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def home(request):
    posts = Article.objects.all()
    return render(request,'blog/home.html',{'posts':posts})


def test(request):
    return HttpResponse('<h1>Test Page</h1>')
