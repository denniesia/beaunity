from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from beaunity.accounts.models import Profile
from beaunity.common.tasks import send_approval_email

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        send_approval_email.delay(
            user_id=instance.id,
            object_type='user'
        )

@receiver(post_save, sender=UserModel)
def add_user_to_default_group(sender, instance,created, **kwargs):
    if created:
        user_group = Group.objects.get(name='User')
        instance.groups.add(user_group)