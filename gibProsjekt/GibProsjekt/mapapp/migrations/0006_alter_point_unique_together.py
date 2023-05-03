# Generated by Django 4.2 on 2023-05-02 12:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mapapp', '0005_alter_point_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='point',
            unique_together={('name', 'lat', 'lon', 'user')},
        ),
    ]