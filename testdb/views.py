from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect
from .models import Lesson
from .models import Student
from .models import Teacher
from .forms import LessonForm
from .forms import StudentForm
from .forms import TeacherForm
#Read Create-Delete Update

# Create your views here.
def read(request):
    lessons = Lesson.objects.all()
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    context = {
        "students" : students,
        "lessons" : lessons,
        "teachers" : teachers,
    }
    return render(request, "read.html", context)

def createLesson(request):
    context = {}
    form = LessonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    context["form"] = form
    return render(request, "create.html", context)

def createStudent(request):
    context = {}
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    context["form"] = form
    return render(request, "create.html", context)

def createTeacher(request):
    context = {}
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    context["form"] = form
    return render(request, "create.html", context)

def deleteLesson(request, id):
    obj = get_object_or_404(Lesson, id=id)
    context = {
        "lesson" : obj
    }
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "delete.html", context)

def deleteStudent(request, id):
    obj = get_object_or_404(Student, id=id)
    context = {
        "student" : obj
    }
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "delete.html", context)

def deleteTeacher(request, id):
    obj = get_object_or_404(Teacher, id=id)
    context = {
        "teacher" : obj
    }
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "delete.html", context)

def updateLesson(request, id):
    obj = get_object_or_404(Lesson, id=id)
    context = {
        "lesson" : obj
    }
    form = LessonForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context["form"] = form
    return render(request, "update.html", context)

def updateStudent(request, id):
    obj = get_object_or_404(Student, id=id)
    context = {
        "student" : obj
    }
    form = StudentForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context["form"] = form
    return render(request, "update.html", context)

def updateTeacher(request, id):
    obj = get_object_or_404(Teacher, id=id)
    context = {
        "teacher" : obj
    }
    form = TeacherForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context["form"] = form
    return render(request, "update.html", context)
