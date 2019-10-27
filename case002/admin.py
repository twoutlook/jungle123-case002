from django.contrib import admin

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Data1
from .models import Data2
from .models import Best



class Data1Resource(resources.ModelResource):
    class Meta:
        model = Data1

class Data1Admin(ImportExportModelAdmin):
    resource_class = Data1Resource
    list_display = ('date1','place', 'worker','thing')
    list_filter = ['place','worker']
    search_fields = ['date1','thing']
   
admin.site.register(Data1, Data1Admin)

class Data2Resource(resources.ModelResource):
    class Meta:
        model = Data2

class Data2Admin(ImportExportModelAdmin):
    resource_class = Data2Resource
    list_display = ('name', 'member','date1','role','points')
    list_filter = ['name','role','member']
    search_fields = ['date1']
   
admin.site.register(Data2, Data2Admin)

class BestResource(resources.ModelResource):
    class Meta:
        model = Best

class BestAdmin(ImportExportModelAdmin):
    resource_class = BestResource
    list_display = ('date1','title','name')
    list_filter = ['title','name',]
    search_fields = ['date1']
   
admin.site.register(Best, BestAdmin)