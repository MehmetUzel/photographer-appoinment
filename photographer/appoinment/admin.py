from django.contrib import admin
from .models import Appoinment,OffDays
from import_export import resources
from import_export.admin import ImportExportModelAdmin

@admin.action(description = 'Approve Selected Appoinments')
def approve_appoinment(modeladmin,request,queryset):
    queryset.update(status='APR')

class AppoinmentResource(resources.ModelResource):
    class Meta:
        model = Appoinment
        fields = ('user__email',)

class AppoinmentAdmin(ImportExportModelAdmin):
    resource_class = AppoinmentResource
    actions = [approve_appoinment]
    list_display = ('date','time','user','status')
    ordering = ('date',)
    list_filter = ('status',)


# class AppoinmentActionAdmin(admin.ModelAdmin):
#     actions = [approve_appoinment]


# Register your models here.
admin.site.register(Appoinment,AppoinmentAdmin)
admin.site.register(OffDays)