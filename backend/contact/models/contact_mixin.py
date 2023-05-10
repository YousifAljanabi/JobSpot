from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from backend.abstract.models import ProvinceChoices


class CommonContactMixins(models.Model):
    class Type(models.TextChoices):
        SEEKER = 'seeker'
        EMPLOYEE = 'employee'
        COMPANY = 'company'
        ADMIN = 'admin'

    user_type = models.CharField(max_length=255, null=True, blank=True, choices=Type.choices)
    contact_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField('العنوان 1', max_length=255, null=True, blank=True)
    phone_number = PhoneNumberField('رقم الهاتف 1', null=True, blank=True)
    occupation = models.CharField(null=True, blank=True, max_length=255)
    dob = models.DateField('تأريخ الميلاد', null=True, blank=True)
    nationality = models.CharField('الجنسية', max_length=255, null=True, blank=True)
    province = models.CharField('المحافظة', max_length=255, null=True, blank=True, choices=ProvinceChoices.choices)
    title = models.CharField('المسمى الوظيفي', max_length=255, null=True, blank=True)
    avatar_url = models.URLField('صورة الملف الشخصي', null=True, blank=True)
    bio = models.TextField('السيرة الذاتية', null=True, blank=True)
    company = models.ForeignKey('contact.Company', on_delete=models.PROTECT, null=True, blank=True,
                                related_name='employees')
    about = models.TextField(max_length=500, blank=True)

    class Meta:
        abstract = True


class EmployeeMixins(models.Model):
    class AcademicDegree(models.TextChoices):
        NONE = 'بدون شهادة', 'بدون شهادة'
        PRIMARY = 'ابتدائية', 'ابتدائية'
        SECONDARY = 'متوسطة', 'متوسطة'
        HIGH = 'إعدادية', 'إعدادية'
        DIPLOMA = 'دبلوم', 'دبلوم'
        HIGHDIPLOMA = 'دبلوم عالي', 'دبلوم عالي'
        BSC = 'بكالوريوس', 'بكالوريوس'
        MSC = 'ماجستير', 'ماجستير'
        PHD = 'دكتوراه', 'دكتوراه'

    class EmploymentTypeChoices(models.TextChoices):
        FullTime = 'دوام كامل', 'دوام كامل'
        PartTime = 'دوام جزئي', 'دوام جزئي'
        Freelance = 'عمل حر', 'عمل حر'
        Internship = 'تدريب', 'تدريب'
        Remote = 'عمل عن بعد', 'عمل عن بعد'

    class IndustryTypeChoices(models.TextChoices):
        Software = 'برمجيات', 'برمجيات'
        Hardware = 'هاردوير', 'هاردوير'
        Networking = 'شبكات', 'شبكات'
        Telecom = 'اتصالات', 'اتصالات'
        Electronics = 'إلكترونيات', 'إلكترونيات'
        Manufacturing = 'تصنيع', 'تصنيع'
        Construction = 'بناء', 'بناء'
        Agriculture = 'زراعة', 'زراعة'
        Education = 'تعليم', 'تعليم'
        Health = 'صحة', 'صحة'
        Tourism = 'سياحة', 'سياحة'
        Media = 'إعلام', 'إعلام'
        Marketing = 'تسويق', 'تسويق'
        Finance = 'مالية', 'مالية'
        Other = 'أخرى', 'أخرى'

    class ExperienceRequiredChoices(models.TextChoices):
        NotRequired = 'لا يشترط', 'لا يشترط'
        OneYear = 'سنة واحدة', 'سنة واحدة'
        TwoYears = 'سنتين', 'سنتين'
        ThreeYears = '3 سنوات', '3 سنوات'
        FiveYears = '5 سنوات', '5 سنوات'
        SevenYears = '7 سنوات', '7 سنوات'
        TenYears = '10 سنوات', '10 سنوات'
