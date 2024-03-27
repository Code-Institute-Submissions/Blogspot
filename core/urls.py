 
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Home Page URL
    path('', views.PostListView.as_view(), name='home'),

    # Post URLs
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    
    # Comment URLs
    path('<slug:slug>/comment/', views.CommentCreateView.as_view(), name='comment_create'),
    path('<slug:slug>/comment/<int:comment_id>/reply/', views.CommentReplyView.as_view(), name='comment_reply'),
    
    
]