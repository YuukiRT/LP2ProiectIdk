from .views import HomeView
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('image_upload/', avatarView, name='image_upload'),
    path('success/', uploadok, name='success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

