from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from beaunity.common.tasks import send_approval_email

@login_required
def approve_instance(request, model_class, pk: int, permission_required: str, redirect_approved, redirect_fallback):
    instance = get_object_or_404(model_class, pk=pk)

    if request.user.has_perm(permission_required):
        instance.is_approved = True
        instance.save()
        send_approval_email.delay(
            instance.created_by.id,
            instance.title
        )
        return redirect(redirect_approved)

    return redirect(redirect_fallback, pk=pk)


@login_required
def disapprove_instance(request, model_class, pk: int, permission_required: str, redirect_disapproved, redirect_fallback):
    instance = get_object_or_404(model_class, pk=pk)

    if request.user.has_perm(permission_required):
        instance.delete()
        return redirect(redirect_disapproved)

    return redirect(redirect_fallback, pk=pk)