# urls.py

from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Home Page URL
    path('', views.PostListView.as_view(), name='home'),

    # Post URLs
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_details'),

    # Like, Dislike, Report URLs
    path('like/<slug:slug>/', views.like_post, name='like_post'),
    path('dislike/<slug:slug>/', views.dislike_post, name='dislike_post'),
    path('report/<slug:slug>/', views.report_post, name='report_post'),

    # log-in URLs
    path('login/', views.custom_login, name='login'),

    # Sign-up URLs
    path('signup/', views.signup, name='signup'),

    # Search URLs
    path('search/', views.search, name='search'),
]
