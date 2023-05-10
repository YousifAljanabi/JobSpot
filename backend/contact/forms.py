from django.contrib.auth.forms import AuthenticationForm
from django.forms import CharField, TextInput, PasswordInput


class LogInForm(AuthenticationForm):
    username = CharField(

        widget=TextInput(
            attrs={
                'autofocus': True,
                'class': 'input border border-white sm:text-sm rounded-lg block w-full p-2.5',
            }))
    password = CharField(

        strip=False,
        widget=PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'class': 'input border border-white sm:text-sm rounded-lg block w-full p-2.5',
            }),
    )

