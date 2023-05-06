from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('company/<int:id>/', views.company, name='company'),
    path('create/<int:id>/', views.create, name='create'),
    path('registration/', views.registration, name='register'),
    path('authentication/', views.auth, name='auth'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.close_log, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)