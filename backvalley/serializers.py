from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Startup, Employee, Sector, Role

class StartupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Startup
        fields = ('logo', 'employees', 'name', 'site', 'city', 'address', 'email', 'phone', 'facebook', 'instagram', 'linkedin', 'mission', 'summary', 'sector', 'lat', 'lon')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'facebook', 'instagram', 'linkedin', 'role')

class SectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sector
        fields = ('name',)

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ('name',)