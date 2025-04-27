from django.contrib import admin

from .models import Doctor, Patient, Visit

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Visit)

