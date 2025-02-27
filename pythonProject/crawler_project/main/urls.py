from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('', views.login, name='login'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
]