# Generated by Django 3.2.18 on 2023-05-06 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_education_institution_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='year',
        ),
        migrations.AddField(
            model_name='education',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاريخ النهايه'),
        ),
        migrations.AddField(
            model_name='education',
            name='expected_graduation_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاريخ التخرج المتوقع'),
        ),
        migrations.AddField(
            model_name='education',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاريخ البدايه'),
        ),
    ]
