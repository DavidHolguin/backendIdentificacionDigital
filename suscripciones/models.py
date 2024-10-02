from django.db import models
from django.conf import settings

class Suscripcion(models.Model):
    PLAN_CHOICES = (
        ('basic', 'Básico'),
        ('premium', 'Premium'),
    )
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.CharField(max_length=10, choices=PLAN_CHOICES, default='basic')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Suscripción de {self.user.username} - Plan {self.plan}"