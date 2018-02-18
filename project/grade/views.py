from django.shortcuts import render
from course.models import Course
from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	PermissionRequiredMixin
	)
from django.contrib.auth import get_user_model
from .models import subject
from django.shortcuts import render
User = get_user_model()
from django.shortcuts import render, get_object_or_404, redirect
from grade.models import Grade
from django.views import generic
from myuser.models import MyUser

from django.views.generic import (ListView,DetailView,CreateView,UpdateView)
# Create your views here.

#BSCS
class bscsfirst(generic.ListView):
	def get(self, request): 
		query = self.request.GET.get('q')
		students = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='1st').search(query)
		context = {'students':students,}
		return render(request, "student_list.html", context)


class bscssecond(generic.ListView):
	def get(self, request): 
		query = self.request.GET.get('q')
		students = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='2nd').search(query)
		context = {'students':students,}
		return render(request, "student_list.html", context)

class bscsthird(generic.ListView):
	def get(self, request): 
		query = self.request.GET.get('q')
		students = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='3rd').search(query)
		context = {'students':students,}
		return render(request, "student_list.html", context)
class bscsfourth(generic.ListView):
	def get(self, request): 
		query = self.request.GET.get('q')
		students = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='4rth').search(query)
		context = {'students':students,}
		return render(request, "student_list.html", context)



