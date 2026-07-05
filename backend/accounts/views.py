from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework.views import APIView

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(
            raise_exception=True
        )

