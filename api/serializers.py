from rest_framework import serializers
from posts.models import Post, Group, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post', 'created', 'author')


class PostSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField(read_only=True, required=False)
    comments = CommentSerializer(many=True, required=False)
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        fields = ('id', 'text', 'author',
                  'image', 'pub_date', 'group', 'comments')
        model = Post
        read_only_fields = ('pub_date', 'author')


class GroupSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description', 'posts')
