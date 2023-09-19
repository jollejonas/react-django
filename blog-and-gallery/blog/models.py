from django.db import models
from django.contrib.auth import get_user_model

   
User = get_user_model()

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    
    # auto_now_add = time at create - auto_now = update time at every modification
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    
class Comment(models.Model):
    comment = models.TextField
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments")