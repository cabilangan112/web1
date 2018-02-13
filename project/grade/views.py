from django.shortcuts import render
from .models import Grade
from course.models import Course
from django.views.generic import (ListView,DetailView,CreateView,UpdateView)

def index(request):
		qs = MyUser.objects.filter(course__course_name__contains='BSCS')
		students =Course.objects.all()
		context = {'students':qs,}
		return render(request, "student_list.html", context)
		
class GradeDetail(DetailView):
	model = Grade
	template_name = "Grade.html"	
	def get_context_data(self, **kwargs):
		context = super(LostDetail, self).get_context_data(**kwargs)
		return context
