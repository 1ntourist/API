from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post


class CommentListSerializers(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'post', 'body', 'created_at',)
        model = Comment


class CommentCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('post', 'author', 'body',)


class UserSelializers(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)