from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . import models

class UserAdmin(admin.ModelAdmin):
	list_display = ("first_name", "last_name", "age", "job_position")


admin.site.register(models.UserReg, UserAdmin)