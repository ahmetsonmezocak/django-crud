from django.urls import path
from . import views

urlpatterns = [
    path("", views.read),
    path("createdelete", views.createdelete),
    path("update", views.update),
]