from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Retrieve published posts
def post_list(request):
    posts = Post.objects.filter(status=1)
    return render(request, 'blog/post_list.html', {'posts': posts})

# Retrieve published post by slug
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)  
    return render(request, 'blog/post_detail.html', {'post': post})

# Bind the POST data to the form
# Create a new comment object but don't save it to the database yet
# Redirect to the post detail page after adding comment
# Create a new blank form
@login_required
def add_comment_to_post(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    if request.method == 'POST':
        form = CommentForm(request.POST)  
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()  
    return render(request, 'blog/add_comment_to_post.html', {'post': post, 'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})
