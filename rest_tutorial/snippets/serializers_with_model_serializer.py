from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Snippet

# Serializing with id
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "snippets"]


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Snippet
        fields = [
            "id",
            "title",
            "code",
            "lineos",
            "language",
            "style",
            "owner",
        ]
