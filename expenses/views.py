from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ExpenseSerializer
from .models import Expenses
from category.models import Category
from rest_framework.exceptions import PermissionDenied
# Create your views here.
class ExpenseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        queryset =  Expenses.objects.filter(user=self.request.user)
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset
    
    def perform_create(self, serializer):
        category = serializer.validated_data['category']
        if category.user != self.request.user:
            raise PermissionDenied("you can't use someone else's category!")
        serializer.save(user=self.request.user)