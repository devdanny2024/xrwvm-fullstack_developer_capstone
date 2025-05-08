"""djangoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),  # Django app API endpoints
    path('', TemplateView.as_view(template_name="Home.html")),  # Home page
    path('about/', TemplateView.as_view(template_name="About.html")),  # About page
    path('login/', TemplateView.as_view(template_name="index.html")),  # React login page
    path('register/', TemplateView.as_view(template_name="index.html")),  # React register page
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
