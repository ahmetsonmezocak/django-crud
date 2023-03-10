from django.db import models

# Create your models here.
class Lesson(models.Model):
    name = models.CharField(max_length=30)

class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    lessons = models.ManyToManyField(Lesson)

class Teacher(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)