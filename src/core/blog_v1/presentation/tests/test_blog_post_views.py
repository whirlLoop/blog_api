"""Blog views tests."""
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from blog_v1.presentation.blog.views import BlogPostDetail
from blog_v1.presentation.tests.common import create_blog_user
from blog_v1.models import BlogPost


class BlogTestCase(APITestCase):
    """Tests Blog services

    Arguments:
        APITestCase {[type]} -- [description]
    """

    def setUp(self):
        """Initialize test parameters.
        """
        self.basic_user = create_blog_user()

    def post_blog(self, title, publish_status):
        """Creates a blog post for testing
        Args:
            title {string} -- Title of the blog
            status {string} -- Publish status
        Returns:
            object -- response object
        """
        url = '/v1/posts/'
        data = {
            "title": title,
            "publish_date": "2020-05-16T02:03:00.716312Z",
            "status": publish_status,
            "author": self.basic_user.pk
            }
        response = self.client.post(url, data, format='json')
        return response

    def test_post_blog_post(self):
        """Test can create a blog entry.
        """
        blog_title = "SpaceX, Mars here we come!"
        blog_status = "draft"
        response = self.post_blog(blog_title, blog_status)
        # print(response.data)
        assert response.status_code == status.HTTP_201_CREATED
        assert BlogPost.objects.count() == 1
        assert BlogPost.objects.get().title == blog_title

    def test_get_blog_posts(self):
        """Test can get a list of blog entries
        """
        blog_one_response = self.post_blog(
            "Blog one",
            "published"
        )
        assert blog_one_response.status_code == status.HTTP_201_CREATED
        blog_two_response = self.post_blog(
            "Blog Two",
            "draft"
        )
        assert blog_two_response.status_code == status.HTTP_201_CREATED
        url = '/v1/posts'
        get_response = self.client.get(url)
        assert get_response.status_code == status.HTTP_200_OK
        self.assertEquals(len(get_response.data), 2)
