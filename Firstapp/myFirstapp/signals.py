from django.db.models.signals import post_save
from django.dispatch import receiver
from myFirstapp.models import Comment, Post
from myFirstapp.notifications import send_notification

@receiver(post_save, sender=Comment)
def notify_post_author(sender, instance, **kwargs):
    post = instance.post
    user = post.user
    comment_user = instance.user
    send_notification(user, f"New comment on your post: {instance.text}")




    