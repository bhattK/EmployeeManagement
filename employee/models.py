from django.db import models

# Create your models here.
class Employee(models.Model):
    fname = models.CharField(max_length=100, blank=True)
    lname = models.CharField(max_length=100, blank=True)
    desig = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    manager = models.CharField(max_length=100, blank=True)

    def _str_(self):
        return self.fname