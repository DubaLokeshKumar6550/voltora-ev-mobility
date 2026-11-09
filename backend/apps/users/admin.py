# pyrefly: ignore[missing-import]
from django.contrib import admin
# pyrefly: ignore[missing-import]
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# pyrefly: ignore[missing-import]
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'role')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = (
        'email', 'username', 'role', 'kyc_status',
        'is_verified_seller', 'is_staff', 'is_active', 'created_at'
    )
    list_filter = ('role', 'kyc_status', 'is_verified_seller', 'is_staff', 'is_active', 'city')
    search_fields = ('email', 'username', 'first_name', 'last_name', 'phone')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'last_login', 'date_joined')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {
            'fields': ('username', 'first_name', 'last_name', 'phone', 'city', 'address', 'avatar')
        }),
        ('Role & Permissions', {
            'fields': (
                'role', 'is_verified_seller',
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('KYC & Verification', {
            'fields': (
                'kyc_status', 'kyc_notes',
                'driving_licence_number', 'driving_licence_doc',
                'id_card_type', 'id_card_number', 'id_card_doc'
            )
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined', 'created_at', 'updated_at')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'role', 'password1', 'password2'),
        }),
    )
