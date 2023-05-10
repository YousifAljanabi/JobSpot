from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import RedirectView

from backend.contact.models import User
from backend.contact.models.company import Company
from backend.contact.models.employee import Experience, Education, Employee
from backend.jobs.models import Job


def index(request):
    jobs = Job.objects.all().order_by('saved')[0:2]
    employees = Employee.objects.all()[0:2]
    context = {
        'jobs': jobs,
        'employees': employees,
    }
    return render(request, 'abstract/home.html', context)


def profile(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user': user,
        'current_user': request.user,
        'experiences': Experience.objects.filter(employee=user),
        'educations': Education.objects.filter(employee=user),
    }
    return render(request, 'home/profile.html', context)


def company_profile(request, company_id):
    context = {
        'company': Company.objects.get(id=company_id),
        'current_user': request.user,

    }
    return render(request, 'home/company_profile.html', context)


def search(request):
    keyword = request.POST.get('q')
    jobs = Job.objects.filter(
        Q(title__icontains=keyword) | Q(about__icontains=keyword)
    )
    companies = Company.objects.filter(contact_name__icontains=keyword)
    employees = Employee.objects.filter(contact_name__icontains=keyword)
    no_results = False if jobs or companies or employees else True
    context = {
        'jobs': jobs,
        'companies': companies,
        'employees': employees,
        'no_results': no_results,

    }
    return render(request, 'home/search.html', context)