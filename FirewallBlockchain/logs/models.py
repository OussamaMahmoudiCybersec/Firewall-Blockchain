from django.db import models

class FirewallLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    source_ip = models.GenericIPAddressField()
    destination_ip = models.GenericIPAddressField()
    action = models.CharField(max_length=20)  # e.g., "ALLOW" or "BLOCK"
    message = models.TextField()
