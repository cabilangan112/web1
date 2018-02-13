from django.shortcuts import render
from .models import MyUser
from course.models import Course
from grade.models import Grade
# Create your views here.

def index(request):
		qs = MyUser.objects.filter(course__course_name__contains='BSCS')
		students = Grade.objects.all()
		context = {'students':qs,}
		return render(request, "student_list.html", context)
		