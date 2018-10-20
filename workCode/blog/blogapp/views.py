from django.shortcuts import render, redirect, HttpResponse
from blogapp.models import Article, Tag
from django.db.models.aggregates import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def page_robot(context, article_list_str, page):
    article_list_str = Paginator(article_list_str, 3)
    try:
        context['article_list'] = article_list_str.page(page)
    except PageNotAnInteger:
        context['article_list'] = article_list_str.page(1)
    except EmptyPage:
        context['article_list'] = article_list_str.page(
            article_list_str.num_pages)
    return context['article_list']


def index(request, page=None):
    context = {}
    article_list_str = Article.objects.all().order_by('add_date')
    context['article_list'] = page_robot(context, article_list_str, page)
    context['tag_list'] = Tag.objects.annotate(num_posts=Count('article'))
    return render(request, 'index.html', context)


def tag(request, tag, page=None):
    context = {}
    article_list_str = Article.objects.filter(tag=tag).order_by(
        'add_date')
    context['article_list'] = page_robot(context, article_list_str, page)
    context['tag_list'] = Tag.objects.annotate(num_posts=Count('article'))
    context['tag_id'] = tag
    return render(request, 'tag.html', context)


def detail(request, post):
    context = {}
    context['article_str'] = Article.objects.filter(id=post)
    context['tag_list'] = Tag.objects.annotate(num_posts=Count('article'))
    return render(request, 'detail.html', context)


def index_login(request):
    context = {}
    if request.method == 'GET':
        form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():  # 必须使用()
            login(request, form.get_user())
            return redirect(to='index')
        else:
            return HttpResponse('not a user')
    context['form'] = form
    return render(request, 'register_login.html', context)


def index_register(request):
    context = {}
    if request.method == 'GET':
        form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():  # 必须使用()
            form.save
            return redirect(to='index_login')
        else:
            return HttpResponse('Woops')
    context['form'] = form
    return render(request, 'register_login.html', context)
