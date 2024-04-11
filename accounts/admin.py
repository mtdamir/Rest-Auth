from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from accounts.models import *


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    model = Organization
    list_display = ('name', )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('username', 'organization', )
