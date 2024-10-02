from rest_framework import serializers
from .models import Carnet

class CarnetSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Carnet
        fields = ['id', 'username', 'membership_type', 'qr_code', 'created_at', 'updated_at']
        read_only_fields = ['qr_code', 'created_at', 'updated_at']