from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
CATEGORY = (
    ("Design","Design"),
    ("Health","Health"),
    ("Music","Music"),
    ("Sport","Sport"),
    ("Travel","Travel"),
    ("Technology","Technology")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_post')
    content = models.TextField()
    category = models.CharField(max_length=200, choices=CATEGORY)
    published = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    tags = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name="Post" , on_delete = models.CASCADE, blank=True, null=True,related_name='comments')
    user = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    comment = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "%s" % self.comment