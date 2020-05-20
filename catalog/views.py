from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework import permissions
from catalog.serializers import LabelSerializer, EventSerializer
from catalog.models import Label, Event, ExtraInfo

import pandas as pd
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


class DataView(View):
    """
    Endpoint to collect an CSV with own data
    """

    def get(self,request): 
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=export.csv'

        queried = [{'Label' : e.label.name, 'Event' : e.name, 'Timestamp' : e.ts} for e in Event.objects.filter(user=self.request.user).all()]

        df = pd.DataFrame(queried)
        df.to_csv(path_or_buf=response,index=False)

        return response #Event.objects.filter(user=self.request.user).all()