from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import CategorySerializer
from .models import Category
from .filters import CategoryFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
