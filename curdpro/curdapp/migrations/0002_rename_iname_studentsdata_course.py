# Generated by Django 4.1.1 on 2022-10-11 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curdapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentsdata',
            old_name='iname',
            new_name='course',
        ),
    ]
