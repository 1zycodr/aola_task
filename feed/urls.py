from django.urls import path
from .views import ListEventsAPIView

urlpatterns = [
    path('events/', ListEventsAPIView.as_view()),
]
