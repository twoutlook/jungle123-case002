from django.contrib import admin

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Data1

class Data1Resource(resources.ModelResource):
    class Meta:
        model = Data1

class Data1Admin(ImportExportModelAdmin):
    resource_class = Data1Resource
    list_display = ('date1','place', 'worker','thing')
    list_filter = ['place','worker']
    search_fields = ['date1','thing']
   
admin.site.register(Data1, Data1Admin)
