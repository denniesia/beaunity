# Generated by Django 5.2.2 on 2025-07-16 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("challenge", "0006_alter_challenge_difficulty"),
    ]

    operations = [
        migrations.AddField(
            model_name="challenge",
            name="is_new",
            field=models.BooleanField(default=False),
        ),
    ]
