from django.contrib.auth.models import User
from django.utils.html import mark_safe,escape
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'
    
    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.user.username),
            escape(self.description),
            escape(self.image),
            escape(self.created_at),
            escape(self.updated_at),

        )

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:30]}'
    
    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.post),
            escape(self.user.username),
            escape(self.text),
            escape(self.created_at),
            escape(self.updated_at),

        )
    
class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} likes {self.post.id}'

class Follow(models.Model):
    follower = models.ForeignKey(Post, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(Post, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.follower.username} follows {self.following.username}'
    