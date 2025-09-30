from django.contrib import admin
from .models import Doctor

#from django.forms import NumberInput
#from django.db import models

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_mvp', 'hire_day')
    list_display_links = ('name', 'email')
    list_editable = ("is_mvp")
    search_fileds = ('name',)
    list_per_page = 25

admin.site.register(Doctor)