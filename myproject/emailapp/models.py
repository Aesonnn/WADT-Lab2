from django.db import models

# Create your models here.

from django.db import models

# Model for storing contacts
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name