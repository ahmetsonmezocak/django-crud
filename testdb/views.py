from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
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

def create(request):
    context = {}
    form = LessonForm(request.POST or None)
    if form.is_valid():
        lessons = Lesson.objects.all()
        context = {
            "lessons" : lessons
        }
        form.save()
        return HttpResponseRedirect("/")

    context["form"] = form
    return render(request, "create.html", context)

def createStudent(request):
    context = {}
    form = StudentForm(request.POST or None)
    if form.is_valid():
        students = Student.objects.all()
        context = {
            "students" : students
        }
        form.save()
        return HttpResponseRedirect("/")

    context["form"] = form
    return render(request, "create.html", context)

def createTeacher(request):
    context = {}
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        teachers = Teacher.objects.all()
        context = {
            "teachers" : teachers
        }
        form.save()
        return HttpResponseRedirect("/")

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
        return HttpResponseRedirect("/")
    return render(request, "delete.html", context)

def deleteStudent(request, id):
    obj = get_object_or_404(Student, id=id)
    context = {
        "student" : obj
    }
    if request.method =="POST":
        students = Student.objects.all()
        context = {
            "students" : students
        }
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "delete.html", context)

def deleteTeacher(request, id):
    obj = get_object_or_404(Teacher, id=id)
    context = {
        "teacher" : obj
    }
    if request.method =="POST":
        teachers = Teacher.objects.all()
        context = {
            "teachers" : teachers
        }
        obj.delete()
        return HttpResponseRedirect("/")
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
  first = request.POST['name']
  lesson = Lesson.objects.get(id=id)
  lesson.name = first
  lesson.save()
  lessons = Lesson.objects.all()
  context = {
    "lessons" : lessons
  }
  return HttpResponseRedirect("/")

def updateStudentAAAAAAAA(request, id):
    obj = get_object_or_404(Student, id=id)
    context = {
        "student" : obj
    }
    form = StudentForm(request.POST or None, instance=obj)
    context["form"] = form
    return render(request, "updateStudent.html", context)

def updateStudent(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Student, id = id)
 
    # pass the object as instance in form
    form = StudentForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "updateStudent.html", context)

def updaterecordstudent(request, id):
    print(request.POST)
    name = request.POST['name']
    surname = request.POST['surname']
    lessons = request.POST['lessons']
    print(lessons)
    student = Student.objects.get(id=id)
    student.name = name
    student.surname = surname
    student.lessons.clear()
    for lesson in request.POST['lessons']:
        student.lessons.add(lesson)
    student.save()
    students = Student.objects.all()
    context = {
        "students" : students
    }
    return render(request, "read.html", context)

def updateTeacherAAAAAAA(request, id):
    obj = get_object_or_404(Teacher, id=id)
    context = {
        "teacher" : obj
    }
    form = TeacherForm(request.POST or None, instance=obj)
    context["form"] = form
    return render(request, "updateTeacher.html", context)

def updateTeacher(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Teacher, id = id)
 
    # pass the object as instance in form
    form = TeacherForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "updateTeacher.html", context)

def updaterecordteacher(request, id):
    print(request.POST)
    name = request.POST['name']
    surname = request.POST['surname']
    lesson = request.POST['lesson']
    print(lesson)
    teacher = Teacher.objects.get(id=id)
    teacher.name = name
    teacher.surname = surname
    teacher.lesson = lesson
    teacher.save()
    teachers = Teacher.objects.all()
    context = {
        "teachers" : teachers
    }
    return render(request, "read.html", context)
#   first = request.POST['first']
#   teacher = Teacher.objects.get(id=id)
#   teacher.name = first
#   teacher.save()
#   teachers = Teacher.objects.all()
#   context = {
#     "teachers" : teachers
#   }
#   return render(request, "read.html", context)