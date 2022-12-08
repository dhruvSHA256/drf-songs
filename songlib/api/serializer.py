from rest_framework import serializers

from .models import Song, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)
        # fields = "__all__"

    def validate(self, data):
        if any(c in data["username"] for c in "!@#$%^&*()_+"):
            raise serializers.ValidationError(
                "Username should not contain special characters"
            )
        return data


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"
