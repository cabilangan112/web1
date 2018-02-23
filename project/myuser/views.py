from django.shortcuts import render
from course.models import Course
from django.shortcuts import redirect
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render
User = get_user_model()
from django.shortcuts import render, get_object_or_404, redirect
from grade.models import Grade
from django.views import generic
from myuser.models import MyUser
from django.utils.decorators import method_decorator
#from .decorators import student_required
from django.views.generic import (ListView,DetailView,CreateView,UpdateView)
# Create your views here.

#BSCS
class bscsfirst(generic.ListView):
	def get(self, request): 
		query = self.request.GET.get('q')
		students = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='1st')
		context = {'students':students,}
		return render(request, "student_list.html", context)


class bscssecond(generic.ListView):
	def get(self, request): 
		query = self.request.GET.get('q')
		students = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='2nd')
		context = {'students':students,}
		return render(request, "student_list.html", context)

class bscsthird(generic.ListView):
	def get(self, request):
	

		query = self.request.GET.get('q')
		students = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='3rd')
		context = {'students':students,}
		return render(request, "student_list.html", context)


class bscsfourth(generic.ListView):

	def get(self, request): 
		query = self.request.GET.get('q')
		students = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='4rth')
		context = {'students':students,}
		return render(request, "student_list.html", context)



