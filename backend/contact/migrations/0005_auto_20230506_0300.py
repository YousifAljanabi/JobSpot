# Generated by Django 3.2.18 on 2023-05-06 00:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='company',
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_enabled', models.BooleanField(default=True)),
                ('is_canceled', models.BooleanField(default=False)),
                ('canceled_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('restored_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extra', models.JSONField(blank=True, default=dict, null=True)),
                ('job_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='المسمي الوظيفي')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='تاريخ البدايه')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='تاريخ النهايه')),
                ('description', models.TextField(blank=True, null=True, verbose_name='الوصف')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='الموقع')),
                ('canceled_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_experience_canceller', to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='contact.company')),
                ('created_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_experience_adder', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='contact.employee')),
                ('restored_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_experience_restorer', to=settings.AUTH_USER_MODEL)),
                ('updated_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='contact_experience_updater', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeMixin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contact.company')),
            ],
        ),
    ]
