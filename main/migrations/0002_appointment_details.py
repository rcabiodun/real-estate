# Generated by Django 5.0 on 2024-02-10 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
