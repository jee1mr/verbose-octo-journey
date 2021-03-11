from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from comment.models import Comment


class CommentTests(APITestCase):
    def test_list_comments(self):
        """
        Ensure we can list comments
        """
        url = reverse('comment-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comment.objects.count(), 0)

