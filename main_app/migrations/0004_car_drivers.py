# Generated by Django 5.0.4 on 2024-04-17 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='drivers',
            field=models.ManyToManyField(to='main_app.driver'),
        ),
    ]
