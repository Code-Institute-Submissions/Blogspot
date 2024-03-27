 
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Home Page URL
    path('', views.PostListView.as_view(), name='home'),

    # Post URLs
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]