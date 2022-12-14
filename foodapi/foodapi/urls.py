"""foodapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path, re_path
from api.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/category/', CatApiView.as_view()),
    path('api/subtype/', SubApiView.as_view()),
    path('api/products/', ProdApiView.as_view()),
    path('api/user/<slug:id>/', UserApiView.as_view()),
    path('api/user/update/<slug:pk>/', UpdateUserData.as_view()),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
