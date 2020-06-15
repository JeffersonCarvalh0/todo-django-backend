from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ['created_by']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = { 'password': { 'write_only': True } }

    # https://stackoverflow.com/a/57430160/6566006
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
