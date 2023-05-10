from backend.contact.models import User, CustomUserManager


class SeekerManager(CustomUserManager):
    def get_queryset(self, *args, **kwargs):
        qs = super(CustomUserManager, self).get_queryset(*args, **kwargs)
        return qs.filter(user_type=User.Type.SEEKER)


class Seeker(User):
    objects = SeekerManager()
    class Meta:
        proxy = True

    def __str__(self):
        return f'{self.contact_name}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, **kwargs):
        self.user_type = User.Type.SEEKER
        super(Seeker, self).save()
