from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . views import RegisterView,MyTokenObtainPairView,LogoutView,WhoAmIView


urlpatterns = [
    path('token/',MyTokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('register/',RegisterView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('whoami/',WhoAmIView.as_view()),

]
