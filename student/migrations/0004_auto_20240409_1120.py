# Generated by Django 3.2.25 on 2024-04-09 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_studentapplication_parentemail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentapplication',
            name='time',
        ),
        migrations.AddField(
            model_name='studentapplication',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
