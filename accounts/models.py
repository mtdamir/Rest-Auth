from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.




class Organization(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)

    class Meta:
        def __str__(self):
            return "a"

    def __str__(self):
        return self.name

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, db_index=True, null=True, blank=True)
    organization = models.ForeignKey(Organization, related_name="organization", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.username)