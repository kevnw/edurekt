from django.db import models

class CCA(models.Model):
    name = models.CharField(primary_key=True,max_length=256, blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return "{}: {}".format(self.name, self.description)