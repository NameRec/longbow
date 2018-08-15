"""longbow_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as django_auth_views

from longbow import views as longbow_views
from auth import views as auth_views

urlpatterns = [
    path('', longbow_views.IndexView.as_view(), name='index'),
    path('login/', django_auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', django_auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', auth_views.signup, name='signup'),
    path('test_details/<int:test_id>', longbow_views.test_details, name='test-details'),
    path('test_start/<int:test_id>', longbow_views.test_start, name='test-start'),
    path('test_passing/<int:passing_id>', longbow_views.test_passing, name='test-passing'),
    path('admin/', admin.site.urls),
]
