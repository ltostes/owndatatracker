from catalog.models import Label, Event, ExtraInfo
from rest_framework import serializers


class LabelSerializer(serializers.ModelSerializer): #HyperlinkedModelSerializer):
    class Meta:
        model = Label
        fields = ['name']


class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ['info']


class EventSerializer(serializers.ModelSerializer):
    label = LabelSerializer()
    extra_infos = ExtraInfoSerializer(read_only=True,many=True)
    class Meta:
        model = Event
        fields = ['label', 'name', 'ts','extra_infos']