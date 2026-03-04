from rest_framework import serializers
from .models import Expenses

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ['id','category','title','description','date','amount']
        read_only_fields = ['created_at']
        
