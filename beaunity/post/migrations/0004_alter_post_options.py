# Generated by Django 5.2.2 on 2025-06-14 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0003_alter_post_banner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"permissions": [("can_approve_post", "Can approve posts")]},
        ),
    ]
