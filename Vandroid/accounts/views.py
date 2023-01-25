from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenViewBase
from .serializers import *
from .models import *

class UserRegister(APIView):
    def post(self, request):
        serialized_data = UserRegisterSerializer(data=request.data)
        data = {}
        if serialized_data.is_valid():
            account = serialized_data.save()
            data['username'] = account.username
            data['email'] = account.email
            refresh = RefreshToken.for_user(account)
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)

            return Response(data)
        return Response(serialized_data.errors)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer



