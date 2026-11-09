from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CustomLoginView,
    RegisterView,
    ProfileView,
    KYCSubmissionView
)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/login/', CustomLoginView.as_view(), name='auth_login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='auth_refresh'),
    path('auth/profile/', ProfileView.as_view(), name='auth_profile'),
    path('auth/kyc/', KYCSubmissionView.as_view(), name='auth_kyc'),
]

