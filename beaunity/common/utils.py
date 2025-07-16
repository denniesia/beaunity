from datetime import timedelta
from django.utils.timezone import now

def mark_new(model):
    current_date = now()
    week_ago = current_date - timedelta(weeks=1)

    model.objects.filter(created_at__range=(week_ago, current_date)).update(is_new=True)
