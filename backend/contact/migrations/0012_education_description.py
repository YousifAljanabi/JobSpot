# Generated by Django 3.2.18 on 2023-05-06 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0011_remove_education_expected_graduation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='الوصف'),
        ),
    ]
