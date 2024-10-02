from django.contrib import admin
from .models import Suscripcion

class SuscripcionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'start_date', 'end_date', 'is_active')
    list_filter = ('plan', 'is_active')
    search_fields = ('user__username', 'plan')

admin.site.register(Suscripcion, SuscripcionAdmin)
