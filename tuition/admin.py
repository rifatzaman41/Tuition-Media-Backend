from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.AvailableTime)
class SpecializatioAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',),}


admin.site.register(models.Specialization,SpecializatioAdmin)
admin.site.register(models.TuitionTeacher)
admin.site.register(models.Review)