"""Contains data schema for the blog"""
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from blog_v1.models.auth import User


class BlogPost(models.Model):
    """Post schema

    Arguments:
        models {class} -- model superclass

    Returns:
        title {str} -- object's title
    """
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(
        max_length=30,
        help_text=_('Title of the blog'),
    )
    slug = models.SlugField(max_length=300, unique_for_date='publish')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts',
        help_text=_('Id of the author'), )
    publish_date = models.DateTimeField(
        default=timezone.now, help_text=_('Date of post publication'))
    created = models.DateTimeField(
        auto_now_add=True, help_text=_('Date created'))
    updated = models.DateTimeField(auto_now=True, help_text=_('Date updated'))
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
        help_text=_('Designates whether the post has been \
            published or it\'s still a draft'),
    )

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.title
