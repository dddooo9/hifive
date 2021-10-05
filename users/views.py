from django.shortcuts import render
from typing import List

from .models import Profile, Camera
import base64


# Create your views here.
def exercise(request):
    profile = Profile.objects.get(user = request.user)
    cameras = Camera.objects.filter(user = request.user)
    length = len(cameras)
    recent = cameras.last()
    first = cameras.first()
    context = {
        'profile': profile,
        'cameras': cameras,
        'recent': recent,
        'first': first,
        'length': length,

    }
    return render(request, 'users/exercise.html', context)

def mypage(request) :
    return render(request, 'users/mypage.html')
