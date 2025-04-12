from rest_framework import serializers
from .models import FirewallLog

class FirewallLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirewallLog
        fields = '__all__'
