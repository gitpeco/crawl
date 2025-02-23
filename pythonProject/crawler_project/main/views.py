# main/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .crawler import run_crawler
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

@login_required
def home(request):
    results = []
    if request.method == 'POST':
        query = request.POST.get('query')
        if query:
            results = run_crawler(query)
    return render(request, 'main/home.html', {'results': results})

@login_required
def search(request):
    results = run_crawler(query=request.GET.get('query', ''))
    return render(request, 'main/search.html', {'results': results})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # 注册成功后跳转到登录页面
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})