import django_filters as filters

from .models import Event


class EventFilter(filters.FilterSet):
    kind = filters.ChoiceFilter(choices=Event.Type.choices, method='filter_kind')

    class Meta:
        model = Event
        fields = ('kind',)

    def filter_kind(self, queryset, name, value):  # noqa
        return queryset.filter(kind__in=[value, Event.Type.ADVERTISEMENT])
