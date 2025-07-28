from django.core.management.base import BaseCommand
import os
import runpy

class Command(BaseCommand):
    help = "Seeds the database with initial data."

    def handle(self, *args, **kwargs):
        base_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'scripts')

        scripts = [
            "seed_groups.py",
            "seed_users_and_groups.py",
            "seed_categories.py",
            "seed_challenges.py",
            "seed_events.py",
            "seed_posts.py",
            "seed_comments.py",
            "seed_likes.py",
            "seed_favourites.py",
        ]

        for script in scripts:
            script_path = os.path.join(base_path, script)
            self.stdout.write(f"Running {script}...")
            runpy.run_path(script_path)
            self.stdout.write(self.style.SUCCESS(f"✅ Finished {script}"))
