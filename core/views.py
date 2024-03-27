from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

# Create your views here.

class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(status=1)
    context_object_name = 'posts'
    template_name = 'blog/index.html'
    paginate_by = 10

# Retrieve published post by slug
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html' 
    context_object_name = 'post'

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

def search_results(request):
    query = request.GET.get('q')
    if query:
        # Perform the search query
        results = Post.objects.filter(title__icontains=query)
    else:
        results = None
    return render(request, 'blog/search_results.html', {'query': query, 'results': results})
