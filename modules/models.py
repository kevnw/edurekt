from django.db import models

from rooms.models import Room

# Create your models here.
class Module(models.Model):
    code = models.CharField(primary_key=True, max_length=16, blank=False)
    name = models.CharField(max_length=256, blank=False)
    description = models.TextField(blank=True)
    time = models.DateTimeField(blank=True, null=True)

    room = models.OneToOneField(Room, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__ (self):
        return "{}: {}".format(self.code, self.name)