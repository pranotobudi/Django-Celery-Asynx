"""django_celery_asynx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from myapp.views import (home_view, 
                        generate_random_user_pull, 
                        generate_random_user_push, 
                        load_flickr_images_pull, 
                        load_flickr_images_push, 
                        check_progress_view,
                        PhotoView,
                        )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('generate-random-user-pull/', generate_random_user_pull),
    path('generate-random-user-push/', generate_random_user_push),
    path('load-flickr-images-pull/', PhotoView.as_view()),
    path('load-flickr-images-push/', load_flickr_images_push),
    path('check-progress-view/', check_progress_view),
]
