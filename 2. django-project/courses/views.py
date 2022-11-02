from django.shortcuts import render

from .models import Course
# Create your views here.

def index(request):
    courses = Course.objects
    return render(request, 'courses/index.html', {'courses' : courses})