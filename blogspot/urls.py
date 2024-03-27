"""
URL configuration for blogspot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),

    # URL pattern for listing all posts
    path('', views.post_list, name='post_list'),

    # URL pattern for viewing a single post
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),

     # URL pattern for adding a comment to a post
    path('post/<slug:slug>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]
