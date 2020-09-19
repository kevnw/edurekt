from django.db import models

# Create your models here.
class Room(models.Model):
    code = models.CharField(primary_key=True, max_length=256, blank=False)
    address = models.TextField(blank=False)
    max_capacity = models.PositiveIntegerField(blank=False, default=1)
    name = models.CharField(max_length=256, blank=False)

    def __str__ (self):
        return "{}: {}".format(self.code, self.name)