from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

@shared_task()
def send_approval_email( user_id, object_title):
    user = get_user_model().objects.get(id=user_id)
    send_mail(
        subject='Your post has been approved',
        message=f'Hi {user},\n\nYour post - {object_title} - has been approved',
        from_email='beaunity@web.com',
        recipient_list=[user.email],
    )
