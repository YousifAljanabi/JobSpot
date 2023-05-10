# Generated by Django 3.2.18 on 2023-05-05 21:44

import backend.contact.models.user
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_education_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seeker',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('contact.user',),
            managers=[
                ('objects', backend.contact.models.user.CustomUserManager()),
            ],
        ),
    ]
