from django.contrib import admin
from .models import Appoinment,OffDays
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class AppoinmentResource(resources.ModelResource):
    class Meta:
        model = Appoinment
        fields = ('user__email',)

class AppoinmentAdmin(ImportExportModelAdmin):
    resource_class = AppoinmentResource


# Register your models here.
admin.site.register(Appoinment,AppoinmentAdmin)
admin.site.register(OffDays)