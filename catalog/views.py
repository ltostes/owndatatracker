from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from catalog.serializers import LabelSerializer, EventSerializer
from catalog.models import Label, Event, ExtraInfo

# Create your views here.


class LabelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]