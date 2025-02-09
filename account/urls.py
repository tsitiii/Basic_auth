from django.urls import path
from .views import UserList, UserDetail, LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/register', UserList.as_view(), name='user-list'),
    path("users/login", LoginView.as_view(), name="login"),
    path('users/register/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]




