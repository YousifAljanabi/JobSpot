# Generated by Django 3.2.18 on 2023-05-06 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_auto_20230506_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='institution_avatar_url',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='صوره المركز'),
        ),
    ]
