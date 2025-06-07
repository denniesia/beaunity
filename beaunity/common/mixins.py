from django.db import models

class LastUpdatedMixin(models.Model):
    last_updated = models.DateTimeField(auto_now=True)