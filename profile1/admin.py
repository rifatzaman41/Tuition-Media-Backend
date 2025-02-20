from django.contrib import admin
from . import models
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display =['user','phone']
    
    def first_name(self, obj):
        return obj.user.first_name
    
    def last_name(self, obj):
        return obj.user.last_name
    
    first_name.admin_order_field = 'user__first_name'
    last_name.admin_order_field = 'user__last_name'
    
    
admin.site.register(models.Student, StudentAdmin)
