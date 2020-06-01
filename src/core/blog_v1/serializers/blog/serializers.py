"""Mediates between blog model instances and python primitives."""
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from rest_framework.routers import SimpleRouter
from blog_v1.models import BlogPost
from django.utils.translation import gettext_lazy as _
from utils.validators import is_empty, is_alphabet_only, is_valid_post


class BlogPostSerializer(serializers.ModelSerializer):
    """Serializes the BlogPost model.
    """
    status = serializers.ChoiceField(
        choices=BlogPost.STATUS_CHOICES,
        error_messages={'invalid_choice': _(
            "Please provide a valid choice! must be either"
            " (draft, published)",), }
    )
    status_description = serializers.CharField(
        source='get_status_display',
        read_only=True
    )
    class Meta:
        model = BlogPost
        fields = (
            'title', 'author', 'publish_date',
            'status', "status_description"
        )

    def validate_title(self, value):
        """Validate title
        Arguments:
            value {string} -- title of post
        Returns:
            value {string} -- validated string
        Raises:
            ValidationError -- Raises an invalid title error
        """
        if is_empty(value):
            raise ValidationError("Title cannot be empty!")
        if not is_valid_post(value):
            raise ValidationError(
                'Invalid characters provided for title!'
            )
        return value


class OptionalSlashRouter(SimpleRouter):

    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()
