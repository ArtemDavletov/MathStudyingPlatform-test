from rest_framework import serializers

from jb_task2.socnet.models import User, Relationship


class GetUserSerializer(serializers.Serializer):
    login = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class UserCreateSerializer(serializers.Serializer):
    login = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class UsersSerializer(serializers.Serializer):
    login = serializers.CharField()
    email = serializers.EmailField()
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class RelationshipSerializer(serializers.Serializer):
    user_login = serializers.CharField()
    friend_login = serializers.CharField()


class RelationshipResponseSerializer(serializers.Serializer):
    user = UsersSerializer()
    friend = UsersSerializer()
