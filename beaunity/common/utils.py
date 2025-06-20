

def user_is_admin_or_moderator(user):
    return user.is_superuser or user.groups.filter(name='Moderator').exists()
