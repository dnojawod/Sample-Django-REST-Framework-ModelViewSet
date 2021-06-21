from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class HeroViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('id', 'name', 'alias')
    search_fields = ('id', 'name', 'alias')
    ordering_fields = ('id', 'name', 'alias')

