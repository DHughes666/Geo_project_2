from django.db import models

# Create your models here.


class Incidence(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name
