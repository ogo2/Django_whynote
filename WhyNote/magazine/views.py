from django.shortcuts import render
from .models import article, Comment, Likes
from profile_user.models import Profile
from .forms import *

def list_magazine(request):
    article_inf = article.objects.all()
    return render(request, 'magazine/article_list.html', {'article': article_inf})
def add_article(request):
    if request.method == 'POST':
        add_form_article = Add_article(request.POST, request.FILES)
        print('fuck')
        if add_form_article.is_valid():
            add = add_form_article.save(commit=False)
            add.name_user = request.user

            add.save()
    else:
        add_form_article = Add_article()
    return render(request, 'magazine/add_article.html', {'form': add_form_article})
def page_magazine(request, share):
    article_inf = article.objects.get(share=share)
    comment_info = Comment.objects.filter(post_name=article_inf.id)
    user_info = Profile.objects.get(user=article_inf.name_user)
    form_class = CommentForm
    if request.method == 'POST':
        comm_form = CommentForm(request.POST)
        print('fuck')
        if comm_form.is_valid():
            add = comm_form.save(commit=False)
            add.user_name = request.user
            add.post_name = article_inf
            # comm_form = comm_form.save(commit=False)
            print('fuck2')
            add.save()
    else:
        comm_form = CommentForm()

    return render(request, 'magazine/article_page.html', {'article': article_inf,
                                                          'user_info': user_info,
                                                          'comment_info': comment_info,
                                                          'comm_user_info': comment_info,
                                                          'form': comm_form})
