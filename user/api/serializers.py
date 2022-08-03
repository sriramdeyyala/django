from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import *
from django.db.models import Q
from django.contrib.auth import authenticate,login
from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import User


class LoginSerializer(serializers.Serializer):
    """
    We will be using username and password for allowing users to login.
    """
    user_name = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        user_name = attrs.get('user_name')
        password = attrs.get('password')
        try:
            user = User.objects.get(Q(username__iexact=user_name) | Q(password__iexact=password))
            if user and not user.is_active:
                raise exceptions.ValidationError('Please activate your account before login')
        except User.DoesNotExist:
            raise exceptions.ValidationError('Invalid Credentials')
        user = authenticate(username=user.username, password=password)
        if not user:
            raise exceptions.ValidationError('Invalid Credentials')
        return attrs

    def authenticate(self):
        user_name = self.data.get('user_name')
        password = self.data.get('password')
        user = User.objects.get(Q(username__iexact=user_name) | Q(email__iexact=user_name))
        user = authenticate(username=user.username, password=password)
        login(self.context.get('request'), user)
        return user

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('first_name','last_name','email')


# register form

class RegisterSerializer(serializers.Serializer):
    """
    we checking the alredy existing user
    """
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get('email')
        try:
            user = User.objects.get(Q(email__iexact=email) )
            if user:
                raise serializers.ValidationError('User with this email already exist ')
        except User.DoesNotExist:
            pass
        return attrs


# modelviews

class ModelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('first_name','last_name','email','username')

    def validate(self, attrs):
        email = attrs.get('email')
        try:
            user = User.objects.get(Q(email__iexact=email) )
            if user:
                raise serializers.ValidationError('User with this email already exist ')
        except User.DoesNotExist:
            pass
        return attrs



# organization

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','email','username')

    def validate(self, attrs):
        email = attrs.get('email')
        try:
            user = User.objects.get(Q(email__iexact=email) )
            if user:
                raise serializers.ValidationError('User with this email already exist ')
        except User.DoesNotExist:
            pass
        return attrs







