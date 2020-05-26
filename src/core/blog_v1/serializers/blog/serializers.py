"""Mediates between blog model instances and python primitives."""
from rest_framework import serializers
from blog_v1.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    """Serializes the BlogPost model.
    """
    class Meta:
        model = BlogPost
        fields = (
            'title', 'slug', 'author', 'author', 'body',
            'publish', 'created', 'updated', 'status'
        )
