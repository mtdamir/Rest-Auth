from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Organization(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, db_index=True, null=True, blank=True)
    organization = models.ForeignKey(Organization, related_name="users", on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    email_verification_code = models.CharField(max_length=6, null=True, blank=True)
    email_verification_code_created_at = models.DateTimeField(null=True, blank=True)
    phone_number_verified = models.BooleanField(default=False)
    phone_verification_code = models.CharField(max_length=6, null=True, blank=True)
    phone_verification_code_created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.username)

    def generate_verification_code(self):
        # TODO
        pass

    def send_email_verification(self):
        # TODO
        pass

    def send_sms_verification(self):
        # TODO
        pass
