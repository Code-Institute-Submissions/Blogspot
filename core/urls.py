from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'core'

urlpatterns = [
    # Home Page URL
    path('', views.PostListView.as_view(), name='home'),
 
    # log-in URLs
    path('login/', views.custom_login, name='login'),

    # log-out URLs
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    
    # Sign-up URLs
    path('signup/', views.signup, name='signup'),

    # Search URLs
    path('search/', views.search, name='search'),

    # Create Post URLs
    path('create/', views.create_post, name='create_post'),
    
    # Post URLs
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_details'),

    # Add Comment URLs
     path('post/<slug:slug>/add_comment/', views.add_comment, name='add_comment'),
    
    # Delete comment URLs
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),

    # Like, Dislike, Report URLs
    path('like/<slug:slug>/', views.like_post, name='like_post'),
    path('dislike/<slug:slug>/', views.dislike_post, name='dislike_post'),
    path('report/<slug:slug>/', views.report_post, name='report_post'),
]
