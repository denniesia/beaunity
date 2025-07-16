from django.contrib.auth.decorators import user_passes_test

# Only allow staff or superusers to change roles
def superuser_required(view_func):
    return user_passes_test(lambda user: user.is_superuser)(view_func)