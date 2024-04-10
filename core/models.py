from django.db import models

class MyOrganization(models.Model):
    name = models.CharField(max_length=100)

