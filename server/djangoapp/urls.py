# server/djangoapp/urls.py

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Login API endpoint (POST handler)
    path(route='login', view=views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),  # <-- new logout route
    path('register', views.registration, name='register'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
