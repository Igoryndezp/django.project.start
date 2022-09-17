from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id",'title','photo')

admin.site.register(Article, ArticleAdmin)