from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'category', 'keywords']
        labels = {
            'title': 'Title',
            'content': 'Content',
            'tags': 'Tags',
            'category': 'Category',
            'keywords': 'Keywords'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {'body': 'Your Comment'}
