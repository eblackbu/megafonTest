from rest_framework import viewsets, mixins

# Create your views here.
from megafon_api import models, serializers


class TariffViewSet(viewsets.ModelViewSet):
    queryset = models.Tariff.objects.all()
    serializer_class = serializers.TariffSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class EventViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    Метод update, partial_update не разрешен.
    """
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
