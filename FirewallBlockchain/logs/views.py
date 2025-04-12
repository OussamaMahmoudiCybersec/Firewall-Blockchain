from rest_framework import generics
from .models import FirewallLog
from .serializers import FirewallLogSerializer

class FirewallLogListCreate(generics.ListCreateAPIView):
    queryset = FirewallLog.objects.all()
    serializer_class = FirewallLogSerializer