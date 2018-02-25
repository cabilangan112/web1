
# Create your views here.
from django.shortcuts import render
from .models import Course,department
from django.views.generic import TemplateView
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


def dep(request):
    obj = department.objects.all()
    context = {'obj': obj}
    return render(request, 'department.html', context)
