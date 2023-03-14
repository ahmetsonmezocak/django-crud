from django.urls import path
from . import views

urlpatterns = [
    path("", views.read),
    path("read", views.read),
    # path("<id>/delete", views.delete),
    path("delete/<int:id>", views.delete),
    path("create", views.create),
    path("update/<int:id>", views.update),
    path("update/updaterecord/<int:id>", views.updaterecord),
]