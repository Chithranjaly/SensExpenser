from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import ExpenseViewSet


router = DefaultRouter()
router.register('',ExpenseViewSet, basename='expenses')

urlpatterns = [
    path('',include(router.urls)),
]
