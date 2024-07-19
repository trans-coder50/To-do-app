from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User
class PostsSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'




class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def save(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        password = validated_data['password']
        password2 = validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password':'Password must match!'})
        user.set_password(password)
        user.save()
        return user
