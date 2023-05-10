from django.shortcuts import render

from backend import settings
from backend.contact.forms import LogInForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

from backend.contact.models import User


class AppLoginView(LoginView):
    form_class = LogInForm
    template_name = 'contact/login.html'

    def get_success_url(self):
        return reverse('home:index')


class AppLogoutView(LogoutView):
    next_page = reverse_lazy('contact:login')


def signup_page(request):
    return render(request, 'contact/signup_type_select.html')




def signup(request, user_type):
    if request.method == 'GET':

        return render(request, 'contact/signup.html', {
            'user_type': user_type,
        })

    if request.method == 'POST':
        if user_type == 'user':
            employee = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                email=request.POST['email'],
                contact_name=request.POST['contact_name'],
                phone_number=request.POST['phone_number'],
                bio=request.POST['bio'],
                company=request.POST['company'],
                about=request.POST['about'],
                avatar_url=request.POST['avatar_url'],
                province=request.POST['province'],
                title=request.POST['title'],
                )
            employee.save()
            return HttpResponseRedirect(reverse('home:index'))
        elif user_type == 'company':
            company = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                email=request.POST['email'],
                contact_name=request.POST['contact_name'],
                phone_number=request.POST['phone_number'],
                bio=request.POST['bio'],
                company=request.POST['company'],
                about=request.POST['about'],
                avatar_url=request.POST['avatar_url'],
                province=request.POST['province'],
                )
            company.save()
            return HttpResponseRedirect(reverse('home:index'))


