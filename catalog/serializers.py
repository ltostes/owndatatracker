from catalog.models import Label, Event, ExtraInfo
from rest_framework import serializers


class LabelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Label
        fields = ['name']


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['label', 'name', 'ts']


class ExtraInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ['extra_info']