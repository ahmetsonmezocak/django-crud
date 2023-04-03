from django import forms
from .models import Lesson
from .models import Student
from .models import Teacher

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = "__all__"

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, lessons):
        return "%s" % lessons.name
    
class CustomMMCF2(forms.ModelChoiceField):
    def label_from_instance(self, lesson):
        return "%s" % lesson.name

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
    lessons = CustomMMCF(
        queryset=Lesson.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"
    lesson = CustomMMCF2(
        queryset=Lesson.objects.all()
    )