"""Blog post logic."""
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
from blog_v1.models import BlogPost
from blog_v1.serializers import BlogPostSerializer


class BlogPostDetail(ViewSetMixin, generics.ListCreateAPIView):
    """Create and fetch all posts.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    name = 'posts'
