from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('contact/', views.contact, name="contact"),
    path('developer/', views.developer, name="developer"),
    path('', views.index, name="index"),
]