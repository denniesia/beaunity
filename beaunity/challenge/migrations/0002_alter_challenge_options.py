
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='challenge',
            options={'permissions': (('can_approve_challenge', 'Can approve challenge'),), 'verbose_name_plural': 'Challenges'},
        ),
    ]
