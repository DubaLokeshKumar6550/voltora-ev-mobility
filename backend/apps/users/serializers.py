from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD

    def validate(self, attrs):
        data = super().validate(attrs)
        # Add extra user claims to response
        data['user'] = {
            'id': self.user.id,
            'email': self.user.email,
            'username': self.user.username,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'role': self.user.role,
            'phone': self.user.phone,
            'city': self.user.city,
            'kyc_status': self.user.kyc_status,
            'is_verified_seller': self.user.is_verified_seller,
            'is_staff': self.user.is_staff,
            'avatar': self.user.avatar.url if self.user.avatar else None,
        }
        return data


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    confirm_password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'username', 'first_name', 'last_name',
            'phone', 'role', 'city', 'password', 'confirm_password'
        ]
        extra_kwargs = {
            'username': {'required': False},
            'first_name': {'required': False},
            'last_name': {'required': False},
        }

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError({"password": "Passwords do not match."})
        
        email = attrs.get('email', '').strip().lower()
        attrs['email'] = email
        if not attrs.get('username'):
            attrs['username'] = email.split('@')[0]
            # Ensure unique username
            base = attrs['username']
            count = 1
            while User.objects.filter(username=attrs['username']).exists():
                attrs['username'] = f"{base}{count}"
                count += 1
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'email', 'username', 'first_name', 'last_name',
            'role', 'phone', 'city', 'address', 'avatar',
            'kyc_status', 'kyc_notes', 'driving_licence_number',
            'driving_licence_doc', 'id_card_type', 'id_card_number',
            'id_card_doc', 'is_verified_seller', 'created_at'
        ]
        read_only_fields = ['id', 'email', 'role', 'kyc_status', 'kyc_notes', 'is_verified_seller', 'created_at']


class UserKYCSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'driving_licence_number', 'driving_licence_doc',
            'id_card_type', 'id_card_number', 'id_card_doc'
        ]

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.kyc_status = 'submitted'
        instance.save()
        return instance
