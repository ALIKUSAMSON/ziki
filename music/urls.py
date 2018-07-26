"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from contacts import views as contacts_views
from accounts import views as accounts_views
from navigation import views as navigation_views
from uploads import views as upload_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', navigation_views.home, name='home'),
    #path('accounts/', include('accounts.urls')),
    path('contacts/', contacts_views.contact, name='contacts'),
    path('audios/', navigation_views.audios_view, name='audios'),
    path('audio/<int:id>/', navigation_views.audio_view, name='audio'),
    path('dashbaord/', navigation_views.dashboard_view, name='dashbaord'),
    path('news', navigation_views.news_view, name='news'),
    path('videos', navigation_views.videos_view, name='videos'),
    path('login/', accounts_views.login_view, name='login'),
    path('signup/', accounts_views.signup_view, name='signup'),
    path('uploads_news/', upload_views.upload_news_view, name='uploads_news'),
    path('upload_music/', upload_views.upload_music_view, name='upload_music'),
    path('upload_image/', upload_views.upload_image_view, name='upload_image'),
    
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)