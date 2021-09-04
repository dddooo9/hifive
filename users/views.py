from django.shortcuts import render
from .models import Profile, Camera
import base64
# Create your views here.
def exercise(request):
    profile = Profile.objects.get(user = request.user)
    cameras = Camera.objects.filter(user = request.user)

    context = {
        'profile':profile,
        'camera':cameras,
    }
    return render(request, 'users/exercise.html', context)
    
def mypage(request):
    return render(request, 'users/mypage.html')
