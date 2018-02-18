from django.shortcuts import render
from .models import subject
from grade.models import Grade
from .utils import unique_slug_generator
from professor.models import professor
from django.shortcuts import render
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView
	)
# Create your views here.
class subjectDetailView(DetailView):
	def get_queryset(self):
		return subject.filter(user=self.request.user)