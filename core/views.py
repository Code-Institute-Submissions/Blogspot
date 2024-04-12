from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Report
from .forms import CommentForm, PostForm, SignupForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:home') 
        else:
            pass
    return render(request, 'account/login.html')

class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    context_object_name = 'posts'
    template_name = 'core/index.html'
    paginate_by = 10

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

class PostDetailView(DetailView):
    model = Post
    template_name = 'core/post_details.html' 
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all().order_by("-created_on")
        context['comments'] = comments
        context['comment_form'] = CommentForm()  # Add an instance of the form to the context
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user  # Associate the comment with the logged-in user
            comment.save()
            return HttpResponseRedirect(reverse('core:post_details', kwargs={'slug': post.slug}))
        else:
            # If the form is invalid, re-render the page with the form and existing comments
            comments = post.comments.all().order_by("-created_on")
            context = {'post': post, 'comments': comments, 'comment_form': comment_form}
            return render(request, self.template_name, context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'core/create.html', {'form': form})