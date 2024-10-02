from rest_framework import serializers
from .models import Suscripcion

class SuscripcionSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Suscripcion
        fields = ['id', 'username', 'plan', 'start_date', 'end_date', 'is_active']
        read_only_fields = ['start_date', 'is_active']