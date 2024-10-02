from django.urls import path
from .views import CarnetCreateView, CarnetDetailView, CarnetValidateView, AdminCarnetUpdateView

urlpatterns = [
    path('create/', CarnetCreateView.as_view(), name='carnet-create'),
    path('detail/', CarnetDetailView.as_view(), name='carnet-detail'),
    path('validate/<str:username>/', CarnetValidateView.as_view(), name='carnet-validate'),
    path('admin/update/<int:pk>/', AdminCarnetUpdateView.as_view(), name='admin-carnet-update'),
]