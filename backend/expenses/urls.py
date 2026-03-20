from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import ExpenseSummaryView, ExpenseViewSet


router = DefaultRouter()
router.register('',ExpenseViewSet, basename='expenses')

urlpatterns = [
    path('summary/',ExpenseSummaryView.as_view(),name="expenseSummary"),
    path('',include(router.urls)),
]
