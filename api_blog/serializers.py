from rest_framework import serializers
from blog.models import Blog_post
from django.contrib.auth.models import User

class BlogPostSerializer(serializers.ModelSerializer):
    blogger_username = serializers.ReadOnlyField(source='blogger.username')
    class Meta:
        model = Blog_post
        fields = ["id", "title", "content", "date_of_origin", "date_of_update", "blogger", "blogger_username"]
        read_only_fields = ['blogger']


class BloggerSerializer(serializers.ModelSerializer):
    blog_post = serializers.SlugRelatedField(many=True, read_only=True, slug_field='api_slug')
    
    class Meta:
        model = User
        fields = ["id", "username", 'blog_post']

