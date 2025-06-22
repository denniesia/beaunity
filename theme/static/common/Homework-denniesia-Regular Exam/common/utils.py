from organizer.models import Organizer

def get_user_obj():
    return Organizer.objects.first()