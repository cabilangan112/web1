from django.shortcuts import render
from .models import Grade
from course.models import Course

def index(request):
		qs = MyUser.objects.filter(course__course_name__contains='BSCS')
		students =Course.objects.all()
		context = {'students':qs,}
		return render(request, "student_list.html", context)
		