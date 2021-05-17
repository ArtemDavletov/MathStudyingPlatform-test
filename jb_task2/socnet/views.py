# Create your views here.
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from jb_task2.socnet.models import User, Relationship
from jb_task2.socnet.serializers import UsersSerializer, GetUserSerializer, RelationshipSerializer, \
    UserCreateSerializer, RelationshipResponseSerializer


class UsersListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response({"users": serializer.data})


class UserView(APIView):
    def get(self, request, login):
        serializer = GetUserSerializer(data={'login': login})
        if serializer.is_valid(raise_exception=True):
            try:
                user = User.objects.filter(login=login).first()
            except AttributeError:
                return Response(status=status.HTTP_404_NOT_FOUND)

        response_serializer = UsersSerializer(user)
        return Response({"users": response_serializer.data})


class UserCreateView(APIView):
    def post(self, request):
        user = request.data

        serializer = UserCreateSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": f"User '{user_saved.login}' created successfully"})


class RelationshipView(APIView):
    def post(self, request):
        serializer = RelationshipSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = User.objects.filter(login=serializer.data.get('user_login')).first()
            friend = User.objects.filter(login=serializer.data.get('friend_login')).first()

            relationship = Relationship.objects.filter(Q(user=user, friend=friend) | Q(user=friend, friend=user))

            if user is None or friend is None \
                    or serializer.data.get('user_login') == serializer.data.get('friend_login') \
                    or len(relationship) != 0:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            relationship_saved = Relationship.objects.create(user=user, friend=friend)

        return Response({"success": f"Users '{relationship_saved.user}' and '{relationship_saved.friend}' are friends"})


class DeleteRelationshipView(APIView):
    def delete(self, request, user_login, friend_login):
        user = User.objects.filter(login=user_login).first()
        friend = User.objects.filter(login=friend_login).first()

        Relationship.objects.filter(Q(user=user, friend=friend) | Q(user=friend, friend=user)).delete()
        return Response({"success": f"Users '{user_login}' and "
                                    f"'{friend_login}' are not friends anymore"})


class RelationshipsListView(APIView):
    def get(self, request):
        relationships = Relationship.objects.all()
        serializer = RelationshipResponseSerializer(relationships, many=True)
        return Response({"relationships": serializer.data})
