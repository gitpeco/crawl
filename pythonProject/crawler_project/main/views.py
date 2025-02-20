# main/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .crawler import run_crawler

# 管理权限检查
def is_superuser(user):
    return user.is_superuser

@login_required
def home(request):
    return render(request, 'main/home.html')

@login_required
def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        results = run_crawler(query)
        return render(request, 'main/results.html', {'results': results})
    else:
        return redirect('home')

@login_required
@user_passes_test(is_superuser)
def user_management(request):
    users = User.objects.all()
    return render(request, 'main/user_management.html', {'users': users})

# 管理员后台修改
@login_required
@user_passes_test(is_superuser)
def admin_home(request):
    return render(request, 'admin/base_site.html')