# Generated by Django 3.1 on 2020-09-10 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_patientnote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientuserprofile',
            name='doctor',
        ),
    ]
