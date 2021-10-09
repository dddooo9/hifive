from django.shortcuts import render
from typing import List

from .models import Profile, Camera
import base64


# Create your views here.
def exercise(request):
    cameras = Camera.objects.filter(user = request.user)
    recent = cameras.last()
    first = cameras.first()
    
    # middle = Camera.objects.exclude(date = recent.date).exclude(date = first.date)
    context = {
        'cameras': cameras,
        'recent': recent,
        'first': first,
        # 'middle': middle,
    }
    return render(request, 'users/exercise.html', context)


def mypage(request) :
    return render(request, 'users/mypage.html')
