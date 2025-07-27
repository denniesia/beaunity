import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beaunity.settings")
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# Example group definitions with permission codenames
GROUPS_PERMISSIONS = {
    "User": [
        "view_appuser", "change_profile", "delete_profile", "view_profile",
        "add_post", "change_post", "delete_post", "view_post",
        "add_comment", "delete_comment", "change_comment", "view_comment",
        "view_event","view_category",
        "add_like", "change_like", "delete_like", "view_like",
        "add_favourite", "change_favourite", "view_favourite", "delete_favourite",
        "add_challenge", "change_challenge", "view_challenge", "delete_challenge",
    ],
    "Moderator": [
        "add_category", "change_category", "delete_category",
        "can_post_without_approval", "can_approve_post",
        "can_approve_challenge",
    ],
    "Organizer": [
        "add_event", "change_event", "delete_event",
        "can_post_without_approval"
    ],
    "Superuser": [

    ],
}

for group_name, permission_codenames in GROUPS_PERMISSIONS.items():
    group, created = Group.objects.get_or_create(name=group_name)
    if created:
        print(f"✅ Created group: {group_name}")
    else:
        print(f"ℹ️ Group already exists: {group_name}")

    # Clear old permissions
    group.permissions.clear()

    # Assign new permissions
    for codename in permission_codenames:
        try:
            perm = Permission.objects.get(codename=codename)
            group.permissions.add(perm)
            print(f"  ➕ Added permission '{codename}' to {group_name}")
        except Permission.DoesNotExist:
            print(f"  ⚠️ Permission not found: '{codename}'")

print("🎉 Done setting up groups and permissions.")
