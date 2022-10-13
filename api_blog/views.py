from blog.models import Blog_post
from .serializers import BlogPostSerializer, BloggerSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissons import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'bloggers': reverse('api_bloggers_list', request=request, format=format),
        'posts': reverse('api_posts_list', request=request, format=format)
    })


class PostsList(generics.ListCreateAPIView):
    queryset = Blog_post.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(blogger=self.request.user)



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog_post.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class BloggersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = BloggerSerializer


class BloggerDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = BloggerSerializer