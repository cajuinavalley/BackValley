from django.contrib import admin
from .models import Startup, Sector, Role, Employee


class StartupAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sector')

class SectorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'facebook', 'instagram', 'linkedin')

admin.site.register(Startup, StartupAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Employee, EmployeeAdmin)