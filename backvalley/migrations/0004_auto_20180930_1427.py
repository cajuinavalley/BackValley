# Generated by Django 2.1.1 on 2018-09-30 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backvalley', '0003_startup_employees'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='lat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='startup',
            name='lon',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='startup',
            name='logo',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]