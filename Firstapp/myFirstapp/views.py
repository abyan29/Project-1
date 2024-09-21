from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from myFirstapp.models import Post, Comment, Like, Follow
from myFirstapp.serializers import PostSerializer, CommentSerializer, LikeSerializer, FollowSerializer

@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    data = request.data
    post = Post.objects.create(
        user=request.user,
        description=data.get('description', ''),
        image=data.get('image')
    )
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    comment = Comment.objects.create(
        post=post,
        user=request.user,
        text=request.data.get('text')
    )
    serializer = CommentSerializer(comment)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_comment(request,comment_id):
    try:
        comment = Comment.objects.get(id=comment_id, user=request.user)
        comment.delete()
        return Response({'message':'sudah terhapus'})
    except comment.DoesNotExist:
        return Response({'error': 'tidak pernah ada '},status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
        return Response({'message': 'Unliked'})
    return Response({'message': 'Liked'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = User.objects.get(id=user_id)
    follow, created = Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
    if not created:
        follow.delete()
        return Response({'message': 'Unfollowed'})
    return Response({'message': 'Followed'})

