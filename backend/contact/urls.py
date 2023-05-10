from backend.contact import views
from django.urls import path

app_name = 'contact'

urlpatterns = [

    path('login/', views.AppLoginView.as_view(), name='login'),
    path('logout/', views.AppLogoutView.as_view(), name='logout'),
    path('signup/<str:user_type>', views.signup, name='signup'),
    path('signup_type_select/', views.signup_page, name='signup_type_select'),


]