import django_filters
from .models import Expenses

class ExpenseFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title',lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description',lookup_expr='icontains')
    date_before = django_filters.DateFilter(field_name='date',lookup_expr='lte')
    date_after = django_filters.DateFilter(field_name='date',lookup_expr='gte')
    category_name = django_filters.CharFilter(field_name='category__category_name',lookup_expr='icontains')
    amount = django_filters.NumberFilter(field_name='amount', lookup_expr='icontains')
    amount_from = django_filters.NumberFilter(field_name='amount',lookup_expr='gte')
    amount_to = django_filters.NumberFilter(field_name='amount',lookup_expr='lte')
    class Meta:
        model = Expenses
        fields = ['title','description','date','category_name']