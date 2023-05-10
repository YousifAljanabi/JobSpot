from django.urls import path
from backend.abstract import views
app_name = 'abstract'

urlpatterns = [
    path('', views.test, name='test'),
]
