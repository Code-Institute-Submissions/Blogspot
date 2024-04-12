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

    # Create Post URLs
    path('create/', views.create_post, name='create_post'),
    
    # Post URLs
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_details'),

    # Add Comment URLs
    path('post/<slug:slug>/add_comment/', views.add_comment, name='add_comment'),

    # View comment URLs
    path('<slug:slug>/comments/', views.view_comments, name='view_comments'),
]