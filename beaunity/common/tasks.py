from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

@shared_task()
def send_approval_email( user_id, object_type, object_title):
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
        }
    }

    send_mail(
        subject=email_templates[object_type]['subject'],
        message=email_templates[object_type]['message'],
        from_email='beaunity@web.com',
        recipient_list=[user.email],

    )