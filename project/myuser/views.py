from django.shortcuts import render
from .models import MyUser
from course.models import Course
from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	PermissionRequiredMixin
	)


from django.contrib.auth import get_user_model

from django.shortcuts import render
User = get_user_model()
from django.shortcuts import render, get_object_or_404, redirect
from grade.models import Grade
from django.views.generic import (ListView,DetailView,CreateView,UpdateView)
# Create your views here.

def index(request):
		qs = MyUser.objects.filter(course__course_name__contains='BSCS')
		students = Grade.objects.all()
		context = {'students':qs,}
		return render(request, "student_list.html", context)
		
class GradeDetail(DetailView):
	model = Grade
	template_name = "Grade.html"	
	def get_context_data(self, **kwargs):
		context = super(GradeDetail, self).get_context_data(**kwargs)
		return context

	def get_object(self):
		last_name = self.kwargs.get("last_name")
		if last_name is None:
			raise Http404
		return get_object_or_404(User, last_name__iexact=last_name, is_active=True)

	def get_context_data(self, *args, **kwargs):
		context =super(GradeDetail, self).get_context_data(*args, **kwargs)
		myuser = context['myuser']