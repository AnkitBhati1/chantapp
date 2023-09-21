# Generated by Django 4.1.5 on 2023-09-21 07:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_delete_chatsession'),
    ]

    operations = [
        migrations.CreateModel(
            name='chatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('user', models.ManyToManyField(related_name='chatroom', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]