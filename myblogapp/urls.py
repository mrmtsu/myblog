from django.urls import path

from . import views

app_name = 'myblog'

urlpatterns = [
  path('', views.index, name='index'),
  path('contact/', views.contact, name='contact'),
  path('contact/complete/', views.complete, name='complete'),
]