from django.urls import path
from . import views

app_name = 'about_us'

urlpatterns = [
    path('create/', views.create_about_us, name='create'),
    path('<int:pk>/edit/', views.edit_about_us, name='edit'),
]