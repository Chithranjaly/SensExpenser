from django.shortcuts import render
from .serializers import RegisterSerializer, MyTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        refresh = RefreshToken(request.data['refresh'])
        refresh.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)

class WhoAmIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({
            'username':request.user.username,
            'id':request.user.id
        })

