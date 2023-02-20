from django.contrib import admin
from .models import Student, StudentProxy


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'marks']


class StudentProxyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'marks']


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentProxy, StudentProxyAdmin)
