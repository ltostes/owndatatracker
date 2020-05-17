from catalog.models import Label, Event, ExtraInfo
from rest_framework import serializers


class LabelSerializer(serializers.ModelSerializer): #HyperlinkedModelSerializer):
    class Meta:
        model = Label
        fields = ['name']

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs


class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ['info']

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs


class EventSerializer(serializers.ModelSerializer):
    extra_infos = ExtraInfoSerializer(read_only=True,many=True)
    class Meta:
        model = Event
        fields = ['label', 'name', 'ts','extra_infos']

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs