from django.db import models

# Create your models here.

class Label(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Event(models.Model):
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    ts   = models.DateTimeField(auto_now_add=True)

class ExtraInfo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    extra_info = models.CharField(max_length=5000)