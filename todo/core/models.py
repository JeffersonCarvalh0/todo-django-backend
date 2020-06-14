from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    created_by = models.ForeignKey('auth.User', related_name='todos', on_delete = models.CASCADE, editable=False)
    created_at = models.DateTimeField(editable=False)

    # Manually insert date on save - https://stackoverflow.com/a/1737078/6566006
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()

        return super().save(*args, **kwargs)
