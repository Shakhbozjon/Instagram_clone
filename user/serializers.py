from rest_framework import serializers

from accounts.models import Profile
from post.models import Post


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'photo', 'data_of_birth', 'first_name', 'last_name', 'bio', 'location')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'picture', 'caption', 'user')
