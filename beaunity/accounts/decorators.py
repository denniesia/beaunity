from django.contrib.auth.decorators import user_passes_test


def superuser_required(view_func):
    return user_passes_test(lambda user: user.is_superuser)(view_func)