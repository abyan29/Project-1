from django.urls import path
from myFirstapp import views

urlpatterns = [
    path('posts/', views.get_posts, name='get_posts'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<int:post_id>/comment/', views.create_comment, name='create_comment'),
    path('posts/<int:post_id>/like/', views.like_post, name='like_post'),
    path('users/<int:user_id>/follow/', views.follow_user, name='follow_user'),
]