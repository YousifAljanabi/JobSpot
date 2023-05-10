from django.db import models
from django.utils import timezone
from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import get_current_authenticated_user


class IntEntity(models.Model):

    class Meta:
        abstract = True

    is_enabled = models.BooleanField(default=True)
    is_canceled = models.BooleanField(default=False)
    canceled_at = models.DateTimeField(editable=False, null=True, blank=True)
    canceled_by = models.ForeignKey('contact.User', null=True, blank=True, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_canceller")
    restored_at = models.DateTimeField(editable=False, null=True, blank=True)
    restored_by = models.ForeignKey('contact.User', null=True, blank=True, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_restorer")
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)
    created_by = CurrentUserField(related_name="%(app_label)s_%(class)s_adder")
    updated_by = CurrentUserField(on_update=True, related_name="%(app_label)s_%(class)s_updater")
    extra = models.JSONField(null=True, blank=True, default=dict)

    def cancel(self):
        self.is_canceled = True
        self.canceled_at = timezone.now()
        self.canceled_by = get_current_authenticated_user()
        self.save()

    def restore(self):

        self.is_canceled = False
        self.restored_by = get_current_authenticated_user()
        self.restored_at = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
