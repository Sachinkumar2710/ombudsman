"""
URL configuration for ombudsman project.

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
from django.urls import path,include
from .views import *
from ombudsman import views


admin.site.site_header="Ombudsman Community Admin"
admin.site.site_title="Ombudsman Commuinty Admin portal"
admin.site.index_title="Welcome to Ombudsman Community"


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home),
    path("index/",home),
    path("about/",about),
    path("services/",services),
    path("careeroption/",careeroption),
    path("helpdesk/",helpdesk),
    path("section2/",section2),
    path("login/",login),
    
   

]
