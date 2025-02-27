# crawler_project/urls.py
from django.contrib import admin
from django.urls import path, include
from main import views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('main.urls')),
    path('register/', views.register, name='register'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('edit-user/<int:user_id>/', views.edit_user, name='edit_user'),
]
