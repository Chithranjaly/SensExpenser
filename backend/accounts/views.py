from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message":"you are authenticated",
            "user":request.user.username
        })
    
class LoginView(APIView):
    def post(self, request):
             username = request.data.get("username")
             password = request.data.get("password")

             user = authenticate(username=username, password=password)

             if user is None:
                  return Response(
                       {"error":"Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
                  )
             
             refresh = RefreshToken.for_user(user)

             response = Response(
                  {"message":"Login successful"}
             )


             response.set_cookie(
                  key=settings.AUTH_COOKIE,
                  value = str(refresh.access_token),
                  httponly=True,
                  secure=settings.AUTH_COOKIE_SECURE,
                  samesite=settings.AUTH_COOKIE_SAMESITE,
             )

             response.set_cookie(
                  key=settings.REFRESH_COOKIE,
                  value = str(refresh),
                  httponly=True,
                  secure=settings.AUTH_COOKIE_SECURE,
                  samesite=settings.AUTH_COOKIE_SAMESITE,
             )
             return response




class RefreshView(APIView):
     def post(self, request):
          refresh_token = request.COOKIES.get("refresh_token")

          if not refresh_token:
               return Response(
                    {"error": "No refresh token"},
                    status=status.HTTP_401_UNAUTHORIZED
               )
          
          try:
               refresh = RefreshToken(refresh_token)
               access_token = str(refresh.access_token)

               response = Response(
                    {"message":"Token refreshed"}
               )

               response.set_cookie(
                    key="access_token",
                    value=access_token,
                    httponly=True,
                    secure=False,
                    samesite="Lax",
               )

               return response
          except Exception:
               return Response(
                    {"error":"Invalid refresh token"},
                    status= status.HTTP_401_UNAUTHORIZED
               )
          

class LogoutView(APIView):
     def post(self, request):
          response = Response(
               {"message":"Logged out"}
          )
          response.delete_cookie("access_token")
          response.delete_cookie("refresh_token")

          return response
     
