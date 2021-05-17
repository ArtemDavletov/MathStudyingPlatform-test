from django.db import models


class User(models.Model):
    login = models.CharField(max_length=127, unique=True)
    email = models.EmailField(max_length=127)
    created = models.DateTimeField(auto_now_add=True)


class Relationship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend')
    timestamp = models.DateField(auto_now_add=True)
