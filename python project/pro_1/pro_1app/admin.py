from django.contrib import admin
from .models import servicedata


class Adminservicedata(admin.ModelAdmin):
    list_display = ['course_no', 'course_name', 'starting_date', 'timings', 'fee', 'duration', 'trainer_name']


admin.site.register(servicedata, Adminservicedata)

