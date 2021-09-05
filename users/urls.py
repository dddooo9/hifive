from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('exercise/', views.exercise, name="exercise"),
    path('mypage/', views.mypage, name="mypage"),
]