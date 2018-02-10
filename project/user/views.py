from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	PermissionRequiredMixin
	)

from django.contrib.auth import get_user_model

from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import (ListView,DetailView,UpdateView,CreateView)

from grade.models import Grade
from .forms import RegisterForm

User = get_user_model()


class Register(CreateView):
	form_class = RegisterForm
	template_name = 'register.html'
	success_url = '/'

	def dispatch(self, *args, **kwargs):
		if self.request.user.is_authenticated():
			return redirect("/logout")
		return super(RegisterView, self).dispatch(*args, **kwargs)