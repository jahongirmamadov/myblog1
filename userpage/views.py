from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
from blog.models import Article

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request,"You were successfully registered!")
            return redirect('blog:blog')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        if user is None:
            messages.success(request,"Username or Password is wrong!")
            return render(request,"login.html",context)
        login(request, user)
        messages.success(request,"You are successfully logged in! ")
        return redirect("blog:blog")
    return render(request,"login.html",context)



def logoutUser(request):
    logout(request)
    messages.success(request,"You are successfully loged out !")
    return redirect("blog:blog")

def cpanel(request):
    articles = Article.objects.filter(author=request.user)
    return render(request,"controlpanel.html",{ "articles": articles})

