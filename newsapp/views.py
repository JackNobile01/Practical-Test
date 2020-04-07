from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def index(request):
    return HttpResponse("Hello, world. You're at the news index.")

def detail(request, article_id):
    return HttpResponse("You're looking at article %s." % article_id)

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date_text')[:5]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'newsapp/index.html', context)