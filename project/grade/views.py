from django.shortcuts import render
from course.models import Course
from django.views.generic import TemplateView
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render
User = get_user_model()
from django.shortcuts import render, get_object_or_404, redirect
from grade.models import Grade
from django.views import generic
from myuser.models import MyUser
from django.utils.decorators import method_decorator
from myuser.decorators import student_required
from .forms import GradeCreate
from django.views.generic import (ListView,DetailView,CreateView,UpdateView)
# Create your views here.

class Year(TemplateView):
    template_name = 'department/Year.html'
    
class ProfileDetailView2(DetailView):
	template_name = 'Grade2.html'

	def get_object(self):
		last_name = self.kwargs.get("last_name")
		if last_name is None:
			raise Http404
		return get_object_or_404(User, last_name__iexact=last_name, is_active=True)

	def get_context_data(self, *args, **kwargs):
		context =super(ProfileDetailView2, self).get_context_data(*args, **kwargs)
		myuser = context['myuser']
		return context


class ProfileDetailView1(DetailView):
	template_name = 'Grade.html'

	def get_object(self):
		last_name = self.kwargs.get("last_name")
		if last_name is None:
			raise Http404
		return get_object_or_404(User, last_name__iexact=last_name, is_active=True)

	def get_context_data(self, *args, **kwargs):
		context =super(ProfileDetailView1, self).get_context_data(*args, **kwargs)
		myuser = context['myuser']
		return context



class ProfileDetailView3(DetailView):
	template_name = 'Grade3.html'

	def get_object(self):
		last_name = self.kwargs.get("last_name")
		if last_name is None:
			raise Http404
		return get_object_or_404(User, last_name__iexact=last_name, is_active=True)

	def get_context_data(self, *args, **kwargs):
		context =super(ProfileDetailView3, self).get_context_data(*args, **kwargs)
		myuser = context['myuser']
		return context

class ProfileDetailView4(DetailView):
	template_name = 'Grad4.html'

	def get_object(self):
		last_name = self.kwargs.get("last_name")
		if last_name is None:
			raise Http404
		return get_object_or_404(User, last_name__iexact=last_name, is_active=True)

	def get_context_data(self, *args, **kwargs):
		context =super(ProfileDetailView4, self).get_context_data(*args, **kwargs)
		myuser = context['myuser']
		return context




class grade_Create(CreateView):

	form_class = GradeCreate
	template_name = 'forms/grade-create.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'student'
		return super().get_context_data(**kwargs)

	def get_queryset(self):
		return Grade.objects.filterfilter(user=self.request.user.is_student)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('/home')
 
