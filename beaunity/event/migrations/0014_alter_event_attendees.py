# Generated by Django 5.2.2 on 2025-07-10 06:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0013_alter_event_is_public"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="attendees",
            field=models.ManyToManyField(
                blank=True, related_name="event_attendees", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
