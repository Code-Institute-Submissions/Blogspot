from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from cloudinary.forms import CloudinaryFileField
from django.utils.text import slugify


class PostForm(forms.ModelForm):
    image = CloudinaryFileField(
        options={
            'folder': 'blog_images/',
            'resource_type': 'image'
        },
        required=False
    )

    excerpt = forms.CharField(
        label='Excerpt',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

    class Meta:
        model = Post
        fields = ['title', 'content', 'excerpt', 'keywords']

    def save(self, commit=True):
        post = super().save(commit=False)
        post.status = 1
        if not post.slug:
            post.slug = slugify(post.title)

        image = self.cleaned_data.get('image', None)
        if image:
            post.featured_image = image

        if commit:
            post.save()
        return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    pass
