from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.utils.timezone import now

from datetime import timedelta
from beaunity.event.models import Event
from beaunity.challenge.models import Challenge
import beaunity.settings as settings


@shared_task()
def send_approval_email( user_id, object_type, object_title=None):
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
    )

@shared_task
def send_reminders():
    two_days_later = now().date() + timedelta(days=2)

    starting_events = Event.objects.filter(
        start_time__date=two_days_later,
    )

    starting_challenges = Challenge.objects.filter(
        start_time__date=two_days_later,
    )

    for event in starting_events:
        users = event.attendees.all()

        for user in users:
            send_mail(
                subject=f"Reminder: {event.title} is in 2 days!",
                message=f"Hello {user.username},\n\n"
                        f"Just a reminder that the event '{event.title}' starts in 2 days on - {event.start_time.strftime('%Y-%m-%d %H:%M')}.\n"
                        f"See you there!",
                from_email = settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
            )

    for challenge in starting_challenges:
        users = challenge.attendees.all()
        for user in users:
            send_mail(
                subject=f"Reminder: Challenge - {challenge.title} - starts in 2 days!",
                message=f"Hello {user.username},\n\n"
                        f"Just a reminder that the challenge '{challenge.title}' starts in 2 days on - {challenge.start_time.strftime('%Y-%m-%d %H:%M')}.\n"
                        f"Get ready to smash it!",
                from_email = settings.EMAIL_HOST_USER ,
                recipient_list=[user.email],
            )