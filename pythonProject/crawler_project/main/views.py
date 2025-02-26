# main/views.py
from django.shortcuts import render
from .crawler import run_crawler
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

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



@login_required
@user_passes_test(lambda user: user.is_superuser)
def manage_users(request):
    users = User.objects.all()
    return render(request, 'admin/manage_users.html', {'users': users})

# main/views.py
@login_required
@user_passes_test(lambda user: user.is_superuser)
def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.is_active = request.POST.get('is_active', False)
        user.is_staff = request.POST.get('is_staff', False)
        user.save()
        return redirect('manage_users')
    return render(request, 'admin/edit_user.html', {'user': user})

# crawler_project/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

@login_required
@user_passes_test(lambda user: user.is_superuser)
def manage_users(request):
    users = User.objects.all()
    return render(request, 'admin/manage_users.html', {'users': users})

@login_required
@user_passes_test(lambda user: user.is_superuser)
def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.is_active = request.POST.get('is_active', False)
        user.is_staff = request.POST.get('is_staff', False)
        user.save()
        return redirect('manage_users')
    return render(request, 'admin/edit_user.html', {'user': user})