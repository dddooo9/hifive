from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def mypage(request):
    return render(request, 'main/mypage.html')

def exercise(request):
    return render(request, 'main/exercise.html')