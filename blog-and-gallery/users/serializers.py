from rest_framework import serializers
from .models import CustomUser

class CustomUserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'password', 'last_login', 'is_superuser', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined')