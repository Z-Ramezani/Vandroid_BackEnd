from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenVerifySerializer
from rest_framework_simplejwt.tokens import RefreshToken, TokenError, UntypedToken
from config import settings
from .models import *

import django.contrib.auth.password_validation as validators
from rest_framework import generics


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extera_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)




class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        #data.update({'type': 'seller'})
        return data

# class LogoutSerializer(serializers.Serializer):
#     refresh = serializers.CharField()

#     def validate(self, attrs):
#         self.token = attrs['refresh']
#         return attrs

#     def save(self, **kwargs):
#         try:
#             RefreshToken(self.token).blacklist()
#         except TokenError:
#             self.fail('bad token')

