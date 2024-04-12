from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='post_dislikes', blank=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, help_text="Comma-separated keywords for better searchability")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.slug)])


class Comment(models.Model):
    post = models.ForeignKey(
        'Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    name = models.CharField(max_length=80, blank=True)
    email = models.EmailField(blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='comment_dislikes', blank=True)
    edited_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.user.username}"

    def like(self, user):
        self.likes.add(user)

    def unlike(self, user):
        self.likes.remove(user)

    def dislike(self, user):
        self.dislikes.add(user)

    def undislike(self, user):
        self.dislikes.remove(user)

    @property
    def likes_count(self):
        return self.likes.count()

    @property
    def dislikes_count(self):
        return self.dislikes.count()

    def edit(self, body):
        self.body = body
        self.edited_on = timezone.now()
        self.save()

    def delete(self):
        self.is_deleted = True
        self.save()

    def is_reply(self):
        return self.parent is not None

    def get_reply_depth(self):
        depth = 0
        parent_comment = self.parent
        while parent_comment is not None:
            depth += 1
            parent_comment = parent_comment.parent
        return depth


class Report(models.Model):
    POST = 'post'
    COMMENT = 'comment'
    REPORT_CHOICES = [
        (POST, 'Post'),
        (COMMENT, 'Comment'),
    ]

    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    reported_item = models.ForeignKey('core.Post', on_delete=models.CASCADE)
    report_type = models.CharField(max_length=10, choices=REPORT_CHOICES)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report {self.report_type} by {self.reporter.username}"


class Photo(models.Model):
    image = CloudinaryField('image')
    alt = models.CharField(max_length=200)
    uploaded = models.DateTimeField(auto_now_add=True)
