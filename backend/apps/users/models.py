from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer / Rider'),
        ('seller', 'Seller / Fleet Owner'),
        ('admin', 'Platform Admin'),
    )

    KYC_STATUS_CHOICES = (
        ('unverified', 'Unverified'),
        ('submitted', 'Submitted / In Review'),
        ('verified', 'Verified Approved'),
        ('rejected', 'Rejected'),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    phone = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=60, default='Hyderabad')
    address = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    # KYC & Documents
    kyc_status = models.CharField(max_length=20, choices=KYC_STATUS_CHOICES, default='unverified')
    kyc_notes = models.TextField(blank=True, help_text="Admin notes on verification")
    driving_licence_number = models.CharField(max_length=50, blank=True)
    driving_licence_doc = models.ImageField(upload_to='kyc/licences/', blank=True, null=True)
    id_card_type = models.CharField(max_length=30, blank=True, default='Aadhaar Card')
    id_card_number = models.CharField(max_length=50, blank=True)
    id_card_doc = models.ImageField(upload_to='kyc/ids/', blank=True, null=True)
    
    is_verified_seller = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.email} ({self.get_role_display()})"
