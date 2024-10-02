from django.urls import path
from .views import SuscripcionCreateView, SuscripcionDetailView, SuscripcionUpdateView, AdminSuscripcionListView

urlpatterns = [
    path('create/', SuscripcionCreateView.as_view(), name='suscripcion-create'),
    path('detail/', SuscripcionDetailView.as_view(), name='suscripcion-detail'),
    path('update/', SuscripcionUpdateView.as_view(), name='suscripcion-update'),
    path('admin/list/', AdminSuscripcionListView.as_view(), name='admin-suscripcion-list'),
]