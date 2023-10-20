from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Article
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
