from rest_framework import serializers
from comment.models import Comment


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'id', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'replies', 'created_at', 'updated_at']
        depth = 1
