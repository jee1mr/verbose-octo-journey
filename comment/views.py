from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CommentSerializer
from .models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed, edited or deleted
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


