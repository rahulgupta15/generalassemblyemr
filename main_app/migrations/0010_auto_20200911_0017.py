# Generated by Django 3.1 on 2020-09-11 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_patientnote_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorpatient',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.patientuserprofile'),
        ),
    ]
