from django.shortcuts import render
from .models import Grade
from course.models import Course
from subject.models import subject
from django.views.generic import (ListView,DetailView,CreateView,UpdateView)


class GradeDetailView(DetailView):
	def get_queryset(self):
		return Grade.objects.all()