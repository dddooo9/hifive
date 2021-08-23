from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name="index"),
    path('mypage/', views.mypage, name="mypage"),
    path('exercise/', views.exercise, name="exercise"),
]