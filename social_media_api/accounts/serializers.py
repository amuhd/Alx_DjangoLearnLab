from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture', 'followers']

    '''def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        user = User(**validated_data)
        user.save()'''  
        
    def create(self, validated_data):
        # Use create_user to properly create a user with hashed password
        user = get_user_model().User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        
        user = User(**validated_data)
        user.save()
        
        Token.objects.create(user=user)
        
        return user
