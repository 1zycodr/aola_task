from rest_framework import generics
from rest_framework.permissions import AllowAny

from .filters import EventFilter
from .models import Event
from .serializers import EventSerializer


class ListEventsAPIView(generics.ListAPIView):
    permission_classes = [
        AllowAny,
    ]
    queryset = Event.objects.all().prefetch_related(
        'user', 'note', 'achievement', 'advertisement'
    )
    serializer_class = EventSerializer
    filterset_class = EventFilter
    search_fields = (
        'note__title',
        'achievement__name',
        'advertisement__title'
    )
