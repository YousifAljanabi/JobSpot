from django.urls import path

from backend.jobs import views

app_name = 'jobs'

urlpatterns = [
    path('view/<int:job_id>/', views.jobs, name='view_job'),
    path('save/<int:job_id>/', views.save, name='save_job'),
    path('apply/<int:job_id>/', views.apply, name='apply_job'),
    path('applicants/<int:job_id>/', views.applicants, name='applicants'),
    path('lists/<int:company_id>/', views.jobs_list, name='jobs_list'),

]
