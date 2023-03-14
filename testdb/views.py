from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from .models import Lesson
from .forms import LessonForm
#Read Create-Delete Update

# Create your views here.
def read(request):
    lessons = Lesson.objects.all()
    context = {
        "lessons" : lessons
    }
    return render(request, "read.html", context)

def create(request):
    context = {}
    form = LessonForm(request.POST or None)
    if form.is_valid():
        lessons = Lesson.objects.all()
        context = {
            "lessons" : lessons
        }
        form.save()
        return render(request, "read.html", context)

    context["form"] = form
    return render(request, "create.html", context)

def delete(request, id):
    obj = get_object_or_404(Lesson, id=id)
    context = {
        "lesson" : obj
    }
    if request.method =="POST":
        lessons = Lesson.objects.all()
        context = {
            "lessons" : lessons
        }
        obj.delete()
        return render(request, "read.html", context)
    return render(request, "delete.html", context)

def update(request, id):
    obj = get_object_or_404(Lesson, id=id)
    context = {
        "lesson" : obj
    }
    form = LessonForm(request.POST or None, instance=obj)
    context["form"] = form
    return render(request, "update.html", context)

def updaterecord(request, id):
  first = request.POST['first']
  lesson = Lesson.objects.get(id=id)
  lesson.name = first
  lesson.save()
  lessons = Lesson.objects.all()
  context = {
    "lessons" : lessons
  }
  return render(request, "read.html", context)