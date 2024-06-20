# myapp/urls.py
from django.urls import path
from .views import my_view
from django.views.generic import TemplateView

urlpatterns = [
    path('my-form/', my_view, name='my_form'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
]
