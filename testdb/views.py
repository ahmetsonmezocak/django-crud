from django.shortcuts import render
from .models import Lesson
#Read Create-Delete Update

# Create your views here.
def read(request):
    lessons = Lesson.objects.all()
    context = {
        "lessons" : lessons
    }
    return render(request, "read.html", context)

def createdelete(request):
    return render(request, "createdelete.html")

def update(request):
    return render(request, "update.html")