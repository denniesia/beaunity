# Generated by Django 5.2.2 on 2025-06-13 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0002_alter_post_banner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="banner",
            field=models.URLField(blank=True, null=True),
        ),
    ]
