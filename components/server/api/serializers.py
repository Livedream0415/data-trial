from api.models import User, Message
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password_hash', 'timestamp']
        read_only_fields = ['id']
        depth = 2


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'text', 'author_id', 'timestamp']
        read_only_fields = ['id']
