from django.urls import path
from .views import FirewallLogListCreate

urlpatterns = [
    path('logs/', FirewallLogListCreate.as_view(), name='log-list'),
]
