# Generated by Django 4.1.1 on 2023-02-11 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_1app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedbackdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('date', models.DateTimeField(max_length=50)),
                ('feedback', models.CharField(max_length=200)),
            ],
        ),
    ]