"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import re_path, path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
<<<<<<< HEAD

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('login/', views.LoginView.as_view(), name='login'),
    re_path('login-new/', views.UserDirectRegistrationView.as_view(), name='login-new'),
    re_path('signup/', views.SignupView.as_view(), name='signup'),
    re_path('test_token/', views.TestTokenView.as_view(), name='test_token'),
=======




urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('login', views.login),
    re_path('login-new', views.UserDirectRegistrationView.as_view(), name="login-new"),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),
>>>>>>> 9c41a4662d2b10315cd7bd6ca92c71e7e500d6e2
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
<<<<<<< HEAD
=======

>>>>>>> 9c41a4662d2b10315cd7bd6ca92c71e7e500d6e2
]


