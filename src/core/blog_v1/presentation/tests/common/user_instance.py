"""Reusable test objects."""
from blog_v1.models.auth import User


def create_blog_user():
    """Create a simple user.

    Returns:
        object -- user instance
    """
    blogger = User.objects.create_user('blogger')
    return blogger
