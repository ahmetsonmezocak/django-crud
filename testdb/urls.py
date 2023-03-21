from django.urls import path
from . import views

urlpatterns = [
    path("", views.read),
    path("read", views.read),
    path("index", views.read),
    path("deleteLesson/<int:id>", views.deleteLesson),
    path("deleteStudent/<int:id>", views.deleteStudent),
    path("deleteTeacher/<int:id>", views.deleteTeacher),
    path("createLesson", views.createLesson),
    path("createStudent", views.createStudent),
    path("createTeacher", views.createTeacher),
    path("updateLesson/<int:id>", views.updateLesson),
    path("updateStudent/<int:id>", views.updateStudent),
    path("updateTeacher/<int:id>", views.updateTeacher),
]