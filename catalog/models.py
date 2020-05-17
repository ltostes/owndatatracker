from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Label(models.Model):
    name = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Event(models.Model):
    label = models.ForeignKey(Label, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=500)
    ts   = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ExtraInfo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='extra_infos')
    info = models.CharField(max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)