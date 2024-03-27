from django.shortcuts import render
from .models import Post, Comment

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(status=1)  # Retrieve published posts
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)  # Retrieve published post by slug
    return render(request, 'blog/post_detail.html', {'post': post})

def add_comment_to_post(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        Comment.objects.create(post=post, name=name, email=email, body=body)
        # Redirect to the post detail page after adding comment
        return redirect('post_detail', slug=post.slug)
    else:
        return render(request, 'blog/add_comment_to_post.html', {'post': post})
