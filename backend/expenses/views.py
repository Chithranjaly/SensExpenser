from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ExpenseSerializer
from .models import Expenses
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework.response import Response
from .filters import ExpenseFilter
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from accounts.permissisons import IsOwner

# Create your views here.
class ExpenseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = ExpenseSerializer
    filterset_class = ExpenseFilter
    filter_backends = [DjangoFilterBackend]

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


class ExpenseSummaryView(APIView):
    permission_classes = [IsAuthenticated]
    

    def get(self,request):
        user_expense = Expenses.objects.filter(user=request.user)

        total_expense = user_expense.aggregate(
            total = Sum('amount')
        )['total'] or 0

        total_transactions = user_expense.count()

        category_summary = (user_expense
                            .values('category__category_name')
                            .annotate(total = Sum('amount'))
                            .order_by('-total'))
        
        return Response({
            "total_expense":total_expense,
            "total_transactions":total_transactions,
            "category_summary":category_summary,
        })

