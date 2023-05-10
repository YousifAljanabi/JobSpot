from django.db import models
from backend.abstract.models import IntEntity
from backend.contact.models import User, CustomUserManager
from backend.contact.models.contact_mixin import EmployeeMixins


class EmployeeManager(CustomUserManager):
    def get_queryset(self, *args, **kwargs):
        qs = super(CustomUserManager, self).get_queryset(*args, **kwargs)
        return qs.filter(user_type=User.Type.EMPLOYEE)




class Employee(User):
    objects = EmployeeManager()

    class Meta:
        proxy = True

    def __str__(self):
        return f'{self.contact_name}'

    @property
    def code(self):
        return f'EMP{str(self.id).zfill(6)}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, **kwargs):
        self.user_type = User.Type.EMPLOYEE
        super(Employee, self).save()


class Education(IntEntity):
    employee = models.ForeignKey('contact.Employee', blank=True, null=True, related_name='education',
                                 on_delete=models.CASCADE)
    institution_name = models.CharField('مركز التحصيل الدراسي', max_length=255, blank=True, null=True)
    # institution_type = models.CharField('نوع المركز', max_length=255, blank=True, null=True,
    #                                     choices=EmployeeMixins.InstitutionType.choices)
    institution_avatar_url = models.URLField('صوره المركز', max_length=255, blank=True, null=True)
    institution_location = models.CharField('موقع المركز', max_length=255, blank=True, null=True)
    principals_subject = models.CharField('القسم العلمي', max_length=255, blank=True, null=True)
    degree = models.CharField('الشهاده العلميه', max_length=255, blank=True, null=True,
                              choices=EmployeeMixins.AcademicDegree.choices)
    start_date = models.DateField('تاريخ البدايه', blank=True, null=True)
    end_date = models.DateField('تاريخ النهايه', blank=True, null=True)
    division = models.CharField('الاختصاص العلمي', max_length=255, blank=True, null=True)
    description = models.TextField('الوصف', blank=True, null=True)


class Experience(IntEntity):
    employee = models.ForeignKey('contact.Employee', blank=True, null=True, related_name='experience',
                                    on_delete=models.CASCADE)
    company = models.ForeignKey('contact.Company', blank=True, null=True, related_name='employee_experience',
                                on_delete=models.CASCADE)
    job_title = models.CharField('المسمي الوظيفي', max_length=255, blank=True, null=True)
    start_date = models.DateField('تاريخ البدايه', blank=True, null=True)
    end_date = models.DateField('تاريخ النهايه', blank=True, null=True)
    description = models.TextField('الوصف', blank=True, null=True)
    location = models.CharField('الموقع', max_length=255, blank=True, null=True)


class Skill(IntEntity):
    name = models.CharField('المهاره', max_length=255, blank=True, null=True)
    level = models.CharField('المستوي', max_length=255, blank=True, null=True)
    description = models.TextField('الوصف', blank=True, null=True)
