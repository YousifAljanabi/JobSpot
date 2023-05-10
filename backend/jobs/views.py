from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from backend.contact.models.company import Company
from backend.contact.models.employee import Employee
from backend.jobs.models import Job


def jobs(request, job_id):
    job = Job.objects.get(pk=job_id)
    company = job.company
    context = {
        'job': job,
        'company': company,
    }
    return render(request, 'jobs/job.html', context)


def save(request, job_id):
    user = Employee.objects.get(id=request.user.id)
    job = Job.objects.get(pk=job_id)
    if user in job.saved.all():
        job.saved.remove(user)
    else:
        job.saved.add(user)
    return HttpResponseRedirect(reverse('jobs:view_job', kwargs={'job_id': job_id}))


def apply(request, job_id):
    user = Employee.objects.get(id=request.user.id)
    job = Job.objects.get(pk=job_id)
    if user in job.applicants.all():
        job.applicants.remove(user)
    else:
        job.applicants.add(user)
    return HttpResponseRedirect(reverse('jobs:view_job', kwargs={'job_id': job_id}))


def applicants(request, job_id):
    job = Job.objects.get(pk=job_id)
    applicants_list = job.applicants.all()
    context = {
        'job': job,
        'applicants': applicants_list,
    }
    return render(request, 'jobs/applicants.html', context)


def jobs_list(request, company_id):
    company = Company.objects.get(pk=company_id)
    job_list = Job.objects.filter(company=company)
    context = {
        'company': company,
        'jobs': job_list,
    }
    return render(request, 'jobs/list.html', context)
