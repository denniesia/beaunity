from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from beaunity.common.tasks import send_approval_email
from django.shortcuts import get_object_or_404


@login_required
def approve_instance(request, model_class, pk: int, content_type:str, permission_required: str, redirect_approved, redirect_fallback):
    instance = get_object_or_404(model_class, pk=pk)

    if request.user.has_perm(permission_required):
        instance.is_approved = True
        instance.save()
        send_approval_email.delay(
            user_id=instance.created_by.id,
            object_type=content_type,
            object_title=instance.title
        )
        return redirect(redirect_approved)

    return redirect(redirect_fallback)


@login_required
def disapprove_instance(request, model_class, pk: int, permission_required: str, redirect_disapproved, redirect_fallback):
    instance = get_object_or_404(model_class, pk=pk)

    if request.user.has_perm(permission_required):
        instance.delete()
        return redirect(redirect_disapproved)

    return redirect(redirect_fallback, pk=pk)