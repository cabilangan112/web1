from django.shortcuts import render
from django.views.generic import TemplateView
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
from .decorators import student_required
from django.views.generic import (ListView,DetailView,CreateView,UpdateView)
from .forms import  StudentSignUpForm
# Create your views here.

def home(request):
    obj = Course.objects.all()
    context = {'obj': obj}
    return render(request, 'home.html', context)

#BSCS
class bscsfirst(generic.ListView):
	def get(self, request): 
		query = self.request.GET.get('q')
		students = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='1st')
		context = {'students':students,}
		return render(request, "student_list.html", context)
@method_decorator([login_required, student_required], name='dispatch')

class bscssecond(generic.ListView):
	def get(self, request): 
		query = self.request.GET.get('q')
		students = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='2nd')
		context = {'students':students,}
		return render(request, "student_list.html", context)
@method_decorator([login_required, student_required], name='dispatch')
class bscsthird(generic.ListView):
	def get(self, request): 

		query = self.request.GET.get('q')
		students = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='3rd')
		context = {'students':students,}
		return render(request, "student_list.html", context)
		
@method_decorator([login_required, student_required], name='dispatch')
class bscsfourth(generic.ListView):

	def get(self, request): 
		query = self.request.GET.get('q')
		students = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='4rth')
		context = {'students':students,}
		return render(request, "student_list.html", context)



class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'forms/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('students:grade')

 


class SignUpView(TemplateView):
    template_name = 'forms/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('faculty:quiz_change_list')
        else:
            return redirect('students:course')
    return render(request, 'home.html')