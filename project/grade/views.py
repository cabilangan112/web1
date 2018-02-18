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

from django.views.generic import (ListView,DetailView,CreateView,UpdateView)
# Create your views here.

#BSCS
class bscsfirst(generic.ListView):
	def get(self, request): 
		qs = subject.objects.filter(grade__user__course__course_name__contains='BSCS',grade__user__Year__contains='1st')
		students = Grade.objects.all()
		context = {'students':qs,}
		return render(request, "student_list.html", context)


class bscssecond(generic.ListView):
	def get(self, request): 
		qs = subject.objects.filter(grade__user__course__course_name__contains='BSCS',grade__user__Year__contains='2nd')
		students = Grade.objects.all()
		context = {'students':qs,}
		return render(request, "student_list.html", context)

class bscsthird(generic.ListView):
	template_name ='student_list.html'
	def get_queryset(self):
		return Grade.objects.filter(user__course__course_name__contains='BSCS',user__Year__contains='2nd')

	def get_context_data(self, *args, **kwargs):
		context =super(bscsthird, self).get_context_data(*args, **kwargs)
		
		query = self.request.GET.get('q')
		grade = Grade.objects.all().exists()
		qs = subject.objects.all().search(query)
		if grade and qs.exists():
			context['students'] = qs
		return context

class bscsfourth(generic.ListView):
	def get(self, request): 
		qs = subject.objects.filter(grade__user__course__course_name__contains='BSCS',grade__user__Year__contains='4rth')
		students = Grade.objects.all()
		context = {'students':qs,}
		return render(request, "student_list.html", context)



