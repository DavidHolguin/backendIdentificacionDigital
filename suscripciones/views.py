from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Suscripcion
from .serializers import SuscripcionSerializer
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

class SuscripcionCreateView(generics.CreateAPIView):
    serializer_class = SuscripcionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        plan = request.data.get('plan')
        
        # Simulación de pago con Stripe
        try:
            charge = stripe.Charge.create(
                amount=1000 if plan == 'basic' else 2000,
                currency='usd',
                description=f'Suscripción {plan} para {user.username}',
                source=request.data.get('stripeToken')
            )
        except stripe.error.CardError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Crear suscripción
        end_date = datetime.now() + timedelta(days=30)
        suscripcion = Suscripcion.objects.create(
            user=user,
            plan=plan,
            end_date=end_date
        )

        serializer = self.get_serializer(suscripcion)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SuscripcionDetailView(generics.RetrieveAPIView):
    serializer_class = SuscripcionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Suscripcion, user=self.request.user)

class SuscripcionUpdateView(generics.UpdateAPIView):
    serializer_class = SuscripcionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Suscripcion, user=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class AdminSuscripcionListView(generics.ListAPIView):
    serializer_class = SuscripcionSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Suscripcion.objects.all()