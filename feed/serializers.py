from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Event, User, Note, Achievement, Advertisement


class Pagination(PageNumberPagination):

    page_size_query_param = 'limit'

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'page': self.page.number,
            'results': data
        })


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        exclude = ('creator',)


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        exclude = ('users',)


class AdvertisementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    note = NoteSerializer()
    achievement = AchievementSerializer()
    advertisement = AdvertisementSerializer()

    class Meta:
        model = Event
        fields = '__all__'
