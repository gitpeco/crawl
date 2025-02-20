# main/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .crawler import run_crawler  # 爬虫函数
# main/views.py
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .crawler import run_crawler  # 爬虫函数

@login_required
def home(request):
    results = []
    if request.method == 'POST':
        query = request.POST.get('query')
        if query:
            results = run_crawler(query)
        else:
            # 如果没有输入，返回空结果
            pass
    return render(request, 'main/home.html', {'results': results})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = AuthenticationForm

class CustomLogoutView(LogoutView):
    next_page = 'login'