from datetime import timedelta
from django.utils.timezone import now

from beaunity.challenge.models import Challenge
from beaunity.event.models import Event


def mark_new(model):
    current_date = now()
    week_ago = current_date - timedelta(weeks=1)

    model.objects.filter(
        created_at__range=(week_ago, current_date)
    ).update(is_new=True)


def get_upcoming_events():
    two_days_later = now().date() + timedelta(days=2)

    return Event.objects.filter(
        start_time__date=two_days_later
    )


def get_upcoming_challenges():
    two_days_later = now().date() + timedelta(days=2)

    return Challenge.objects.filter(
        start_time__date=two_days_later
    )


def send_reminder_email(user, title, start_time, item_type):
    start_time_str = start_time.strftime('%Y-%m-%d %H:%M')

    if item_type == "event":
        subject = f"BEAUNITY Reminder: {title} is in 2 days!"
        message = (
            f"Hello {user.username},\n\n"
            f"Just a reminder that the event '{title}' starts in 2 days on - {start_time_str}.\n"
            f"See you there!"
        )
    elif item_type == 'challenge':
        subject = f"BEAUNITY Reminder: Challenge - {title} - starts in 2 days!"
        message = (
            f"Hello {user.username},\n\n"
            f"Just a reminder that the challenge '{title}' starts in 2 days on - {start_time_str}.\n"
            f"Get ready to smash it!"
        )

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=True,
    )
