from django.urls import path
from . import views

urlpatterns = [
    path("", views.read),
    path("read", views.read),
    path("index", views.read),
    # path("<id>/delete", views.delete),
    path("delete/<int:id>", views.delete),
    path("deleteStudent/<int:id>", views.deleteStudent),
    path("deleteTeacher/<int:id>", views.deleteTeacher),
    path("create", views.create),
    path("createStudent", views.createStudent),
    path("createTeacher", views.createTeacher),
    path("update/<int:id>", views.update),
    path("update/updaterecord/<int:id>", views.updaterecord),
    path("updateStudent/<int:id>", views.updateStudent),
    path("updateStudent/updaterecordstudent/<int:id>", views.updaterecordstudent),
    path("updateTeacher/<int:id>", views.updateTeacher),
    path("updateTeacher/updaterecordteacher/<int:id>", views.updaterecordteacher),
]