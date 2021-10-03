from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('developer/', views.developer, name="developer"),
    path('communicate/', views.paging, name="paging"),
    path('communicate/<int:question_id>/', views.detail, name='detail'),
    path('communicate/question_create/', views.question_create, name='question_create'),
    path('communicate/answer_create/<int:question_id>/', views.answer_create, name='answer_create'),
]