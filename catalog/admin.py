from django.contrib import admin
from .models import Label, Event, ExtraInfo

# Register your models here.

admin.site.register(Label)
admin.site.register(Event)
admin.site.register(ExtraInfo)