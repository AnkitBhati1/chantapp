# Generated by Django 4.1.5 on 2023-09-20 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChatSession',
        ),
    ]
