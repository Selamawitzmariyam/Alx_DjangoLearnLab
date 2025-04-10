from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = post.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.request.data['post'])
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        comment = self.get_object()
        if comment.author != self.request.user:
            raise PermissionError("You can only edit your own comments.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionError("You can only delete your own comments.")
        instance.delete()
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']