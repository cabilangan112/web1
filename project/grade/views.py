from django.shortcuts import render
from course.models import Course
from django.conf import settings
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
from django.views.generic import (ListView,DetailView,CreateView,UpdateView)
# Create your views here.


class ProfileDetailView(DetailView):
	template_name = 'Grade.html'

	def get_object(self):
		last_name = self.kwargs.get("last_name")
		if last_name is None:
			raise Http404
		return get_object_or_404(User, last_name__iexact=last_name, is_active=True)

	def get_context_data(self, *args, **kwargs):
		context =super(ProfileDetailView, self).get_context_data(*args, **kwargs)
		myuser = context['myuser']
		return context
method_decorator([login_required, student_required], name='dispatch')