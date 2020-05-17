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
    serializer_class = LabelSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Label.objects.filter(user=self.request.user).all()


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
        
    def get_queryset(self): 
        return Event.objects.filter(user=self.request.user).all()

    