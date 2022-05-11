"""password_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

# from django.contrib import admin  # delete it, and make our own page
from django.urls import path
from generator import views     # 1) import this view

# empty string---home page
urlpatterns = [
    # path('admin/', admin.site.urls),      # delete it, and make our own page
    # path('hithere/', admin.site.urls),    # if we can change the name of sub-dir
    path('', views.home, name='home'),     # 2) call function from views
    # path('eggs', views.eggs),
    path('password/', views.password, name='password'),
    path('about/', views.about, name='about'),
]
