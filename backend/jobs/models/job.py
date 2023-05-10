from django.db import models

from backend.abstract.models import IntEntity
from backend.contact.models import EmployeeMixins
from djmoney.models.fields import MoneyField


# Create your models here.


class Job(IntEntity):
    company = models.ForeignKey('contact.Company', on_delete=models.CASCADE, related_name='company_jobs')
    title = models.CharField('العنوان', max_length=255, blank=True, null=True)
    about = models.TextField('الوصف', blank=True, null=True)
    responsibilities = models.TextField('المسؤوليات', blank=True, null=True)
    # skills = models.TextField('المهارات', blank=True, null=True)
    applicants = models.ManyToManyField('contact.employee', blank=True, related_name='jobs')
    saved = models.ManyToManyField('contact.employee', blank=True, related_name='saved_jobs')
    industry = models.CharField('الصناعه', max_length=255, blank=True, null=True,
                                choices=EmployeeMixins.IndustryTypeChoices.choices)
    employment_type = models.CharField('نوع التوظيف', max_length=255, blank=True, null=True,
                                        choices=EmployeeMixins.EmploymentTypeChoices.choices)
    experience = models.CharField('الخبره', max_length=255, blank=True, null=True,
                                    choices=EmployeeMixins.ExperienceRequiredChoices.choices)
    salary = MoneyField('الراتب', max_digits=14, decimal_places=2, default_currency='USD', blank=True, null=True)
    skills = models.ManyToManyField('contact.skill', blank=True, related_name='skills_jobs')

    def __str__(self):
        return f'{self.title} - {self.company} {self.employment_type}'