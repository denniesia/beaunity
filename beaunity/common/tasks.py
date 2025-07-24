from datetime import timedelta

from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils.timezone import now

import beaunity.settings as settings
from beaunity.challenge.models import Challenge
from beaunity.common.utils import (get_upcoming_challenges,
                                   get_upcoming_events, mark_new,
                                   send_reminder_email)
from beaunity.event.models import Event


@shared_task()
def send_approval_email(user_id, object_type, object_title=None):
    User = get_user_model()
    user = User.objects.get(id=user_id)

    email_templates = {
        'post': {
            'subject': 'Your post has been approved',
            'message': f'Hi {user.username},\n\nYour post "{object_title}" has been approved!'
        },
        'challenge': {
            'subject': 'Challenge submission approved',
            'message': f'Hi {user.username},\n\nYour challenge "{object_title}" is now live!'
        },
        'user': {
            'subject': "Welcome to beaunity!",
            'message': f"Hi {user.username},\n\nWe're excited to have you on board."
        }
    }

    send_mail(
        subject=email_templates[object_type]['subject'],
        message=email_templates[object_type]['message'],
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=True
    )


@shared_task
def send_reminders():
    events = get_upcoming_events()
    challenges = get_upcoming_challenges()

    for event in events:
        for user in event.attendees.all():
            send_reminder_email(user, event.title, event.start_time, "event")

    for challenge in challenges:
        for user in challenge.attendees.all():
            send_reminder_email(user, challenge.title, challenge.start_time, "challenge")


@shared_task
def update_is_new_status():
    mark_new(Event)
    mark_new(Challenge)