"""
URL configuration for text_editor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from editor.views import signup, document_list
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', document_list, name='document_list'),
    path('admin/', admin.site.urls),
    path('accounts/signup/', signup, name='signup'),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('documents/', include('editor.urls')),
]