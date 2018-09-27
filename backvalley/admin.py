from django.contrib import admin
from .models import Startup, Sector, Role, Employee

admin.site.register(Startup)
admin.site.register(Sector)
admin.site.register(Role)
admin.site.register(Employee)