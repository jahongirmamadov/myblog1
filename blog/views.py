from django.shortcuts import render,redirect,get_object_or_404
from .models import Article,Comment
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def homepage(request):
    return render(request,"homepage.html")



def home(request):
    return render(request,"home.html")

def cpanel(request):
    return render(request,"controlpanel.html")


@login_required(login_url="userpage:register")
def add(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Hello!!!")
        return redirect("blog:blog")

    return render(request,"add.html",{"form": form})

@login_required(login_url="userpage:register")
def detail(request,id):
    article = get_object_or_404(Article,id = id)
    comments = article.comments.all()

    return render(request,"detail.html",{"article":article, "comments": comments})

@login_required(login_url="userpage:register")
def update(request,id):

    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = str(request.user)
        article.save()
        messages.success(request,"Done!!!")
        return redirect("userpage:cpanel")

    return render(request,"update.html",{"form":form})

@login_required(login_url="userpage:register")
def delete(request,id):
    article = get_object_or_404(Article,id = id)
    article.delete()
    messages.success(request,"Deleted!")
    return redirect("userpage:cpanel")

def articles(request):
    keywords = request.GET.get("keywords")

    if keywords:
        articles =Article.objects.filter(title__contains=keywords)
        return render(request,"articles.html",{"articles":articles})

    articles = Article.objects.all()


    return render(request,"articles.html",{"articles":articles})

def comment(request,id):
    article = get_object_or_404(Article, id = id)
    if request.method =="POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author = comment_author,comment_content =comment_content)
        newComment.article = article
        newComment.save()

    return redirect("/blog/article/" + str(id))



