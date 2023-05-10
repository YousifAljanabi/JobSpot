from django.contrib import admin

from backend.contact.models import User
from backend.contact.models.company import Company
from backend.contact.models.employee import Employee, Experience, Education
from backend.contact.models.seeker import Seeker

# Register your models here.
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Seeker)
admin.site.register(Company)
admin.site.register(Experience)
admin.site.register(Education)
# admin.site.register(Skills)
