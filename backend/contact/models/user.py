from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from backend.abstract.models import IntEntity
from backend.contact.models.contact_mixin import CommonContactMixins


class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = f'{self.model.USERNAME_FIELD}__iexact'
        return self.get(**{case_insensitive_username_field: username})

    def create_user(self, contact_name, email, password=None, type=None):
        if not email:
            raise ValueError('user must have email')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.contact_name = contact_name
        user.is_active = False
        user.user_type = type
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if not email:
            raise ValueError('user must have email')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.user_type = 'admin'
        user.save(using=self._db)
        return user


class User(IntEntity, AbstractUser, CommonContactMixins):
    username = models.NOT_PROVIDED
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name_plural = 'users'
        verbose_name = 'user'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.contact_name}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, **kwargs):
        super(User, self).save()

