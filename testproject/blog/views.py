from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def home(request):
    posts = Article.objects.all()
    res = '<h1>Список статей</h1>'
    for post in posts:
        res += f'<div><h3>{post.title}</h3><div>{post.content}</div><div>{post.photo}</div></div><hr>'
    return HttpResponse(res)

def test(request):
    return HttpResponse('<h1>Test Page</h1>')
