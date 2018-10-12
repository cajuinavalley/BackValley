from django.db import models

# Create your models here.

class Sector(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)

    role = models.ManyToManyField(
        Role,
    )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Startup(models.Model):
    logo = models.ImageField(default='')

    employees = models.ManyToManyField(
        Employee,
    )

    name = models.CharField(max_length=100, default='', blank=False)
    site = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=False)
    address = models.TextField(default='', blank=True)

    lat = models.FloatField(default=0.0, blank=False)
    lon = models.FloatField(default=0.0, blank=False)

    email = models.EmailField(default='', blank=False)
    phone = models.CharField(max_length=100, default='', blank=True)

    facebook = models.CharField(max_length=100, default='', blank=True)
    instagram = models.CharField(max_length=100, default='', blank=True)
    linkedin = models.CharField(max_length=100, default='', blank=True)

    mission = models.TextField(default='', blank=True)
    summary = models.TextField(default='', blank=True)

    sector = models.ForeignKey(
        Sector,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name