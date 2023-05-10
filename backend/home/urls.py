from django.urls import path

from backend.home import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('company/<int:company_id>/', views.company_profile, name='company_profile'),
    path('search/', views.search, name='search'),
]
