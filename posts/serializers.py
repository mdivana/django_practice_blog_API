from rest_framework import serializers

from .models import Post


class PostSerialzier(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created_at",
        )
        model = Post
