# Generated by Django 4.1.1 on 2022-10-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('company', models.CharField(max_length=20)),
            ],
        ),
    ]
