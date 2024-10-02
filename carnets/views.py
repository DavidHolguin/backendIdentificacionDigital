from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Carnet
from .serializers import CarnetSerializer
from django.shortcuts import get_object_or_404

class CarnetCreateView(generics.CreateAPIView):
    serializer_class = CarnetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CarnetDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = CarnetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Carnet, user=self.request.user)

class CarnetValidateView(generics.RetrieveAPIView):
    serializer_class = CarnetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        username = self.kwargs.get('username')
        return get_object_or_404(Carnet, user__username=username)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'is_valid': True,
            'carnet': serializer.data
        })

class AdminCarnetUpdateView(generics.UpdateAPIView):
    serializer_class = CarnetSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Carnet.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)