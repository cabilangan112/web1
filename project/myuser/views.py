from django.shortcuts import render
from .models import MyUser
from course.models import Course
from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	PermissionRequiredMixin
	)


from django.contrib.auth import get_user_model
from subject.models import subject
from django.shortcuts import render
User = get_user_model()
from django.shortcuts import render, get_object_or_404, redirect
from grade.models import Grade
from django.views import generic

from django.views.generic import (ListView,DetailView,CreateView,UpdateView)
# Create your views here.

#BSCS
class bscsfirst(generic.ListView):
	def get(self, request): 
		qs = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='1st')
		students = Grade.objects.all()
		context = {'students':qs,}
		return render(request, "student_list.html", context)

class bscssecond(generic.ListView):
	def get(self, request): 
		qs = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='2nd')
		students = Grade.objects.all()
		context = {'students':qs,}
		return render(request, "student_list.html", context)

class bscsthird(generic.ListView):
	def get(self, request): 
		qs = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='3rd')
		students = Grade.objects.all()
		context = {'students':qs,}
		return render(request, "student_list.html", context)
		
class bscsfourth(generic.ListView):
	def get(self, request): 
		qs = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='4rth')
		students = Grade.objects.all()
		context = {'students':qs,}
		return render(request, "student_list.html", context)


#BSIT

class bsitfirst(generic.ListView):
	def get(self, request): 
		qs = MyUser.objects.filter(course__course_name__contains='BSIT',Year__contains='1st')
		students = Grade.objects.all()
		context = {'students':qs,}
		return render(request, "student_list.html", context)

class bsitsecond(generic.ListView):
	def get(self, request): 
		qs = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='2nd')
		students = Grade.objects.all()
		context = {'students':qs,}
		return render(request, "student_list.html", context)

class bsitthird(generic.ListView):
	def get(self, request): 
		qs = MyUser.objects.filter(course__course_name__contains='BSIT',Year__contains='3rd')
		students = Grade.objects.all()
		context = {'students':qs,}
		return render(request, "student_list.html", context)
		
class bsitfourth(generic.ListView):
	def get(self, request): 
		qs = MyUser.objects.filter(course__course_name__contains='BSIT',Year__contains='4rth')
		students = Grade.objects.all()
		context = {'students':qs,}
		return render(request, "student_list.html", context)


