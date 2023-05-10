# Generated by Django 3.2.18 on 2023-05-08 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0013_skill'),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='saved',
            field=models.ManyToManyField(blank=True, related_name='saved_jobs', to='contact.Employee'),
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_jobs', to='contact.company'),
        ),
    ]