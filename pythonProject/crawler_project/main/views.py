# main/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .crawler import run_crawler

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