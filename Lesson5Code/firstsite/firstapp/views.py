from django.shortcuts import render, redirect
from firstapp.models import Ariticle, Comment
from firstapp.form import CommentForm


def index(request):
    queryset = request.GET.get('tag')
    if queryset:
        ariticle_list = Ariticle.objects.filter(tag=queryset)
    else:
        ariticle_list = Ariticle.objects.all()
    context = {}
    context['ariticle_list'] = ariticle_list
    index_page = render(request, 'first_web_2.html', context)
    return index_page


def detail(request, page_num, error_form=None):
    article = Ariticle.objects.get(id=page_num)
    form = CommentForm  # 仅用于生成表单
    context = {}
    best_comment = Comment.objects.filter(best_comment=True, belong_to=article)
    if best_comment:
        context['best_comment'] = best_comment[0]
    context['article'] = article  # 传输的东西包含表单
    if error_form is not None:
        context['form'] = error_form
    else:
        context['form'] = form
    return render(request, 'article_detail.html', context)


def detail_comment(request, page_num):
    article = Ariticle.objects.get(id=page_num)
    form = CommentForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        comment_str = Comment(name=name, comment=comment, belong_to=article)
        comment_str.save()
    else:
        return detail(request, page_num, error_form=form)
    return redirect(to='detail', page_num=page_num)
