 
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Home Page URL
    path('', views.PostListView.as_view(), name='home'),

    #Search Bar URL
    path('search/', views.search_results, name='search_results'),

    # Post URLs
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    
    # Tag URLs
    path('tag/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
    
    # Comment URLs
    path('<slug:slug>/comment/', views.CommentCreateView.as_view(), name='comment_create'),
    path('<slug:slug>/comment/<int:comment_id>/reply/', views.CommentReplyView.as_view(), name='comment_reply'),
    
    # Like/Dislike Post URLs
    path('<slug:slug>/like/', views.PostLikeView.as_view(), name='post_like'),
    path('<slug:slug>/dislike/', views.PostDislikeView.as_view(), name='post_dislike'),
    
    # Like/Dislike Comment URLs
    path('<slug:slug>/comment/<int:comment_id>/like/', views.CommentLikeView.as_view(), name='comment_like'),
    path('<slug:slug>/comment/<int:comment_id>/dislike/', views.CommentDislikeView.as_view(), name='comment_dislike'),
]