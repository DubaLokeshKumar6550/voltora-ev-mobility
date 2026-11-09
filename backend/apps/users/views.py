from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_spectacular.utils import extend_schema, OpenApiResponse
from .models import User
from .serializers import (
    CustomTokenObtainPairSerializer,
    UserRegistrationSerializer,
    UserProfileSerializer,
    UserKYCSubmissionSerializer,
)

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    @extend_schema(
        summary="User Login with JWT",
        description="Authenticate user with email and password to receive access and refresh JWT tokens and user profile details.",
        responses={200: OpenApiResponse(description="Successful authentication")}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Register New User",
        description="Create a new customer or seller/owner account.",
        responses={201: UserRegistrationSerializer}
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "message": "Account created successfully!",
            "user": {
                "id": user.id,
                "email": user.email,
                "username": user.username,
                "role": user.role,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
        }, status=status.HTTP_201_CREATED)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Get or Update Current User Profile",
        description="Fetch or edit profile information of authenticated user."
    )
    def get_object(self):
        return self.request.user


class KYCSubmissionView(generics.UpdateAPIView):
    serializer_class = UserKYCSubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Submit KYC Documents",
        description="Upload Driving Licence and Government ID proof for verification."
    )
    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response({
            "message": "KYC documents submitted successfully. Verification is in progress.",
            "kyc_status": self.request.user.kyc_status
        })
