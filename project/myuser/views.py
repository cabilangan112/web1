from django.shortcuts import render
from django.views.generic import TemplateView
from course.models import Course,department
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
from course.models import Course
from django.utils.decorators import method_decorator
from .decorators import student_required,teacher_required
from django.views.generic import (ListView,DetailView,CreateView,UpdateView)
from .forms import  UserCreationForm,facultyCreationForm
# Create your views here.

class SignUpView(TemplateView):
    template_name = 'forms/signup.html'


class department(TemplateView):
    template_name = 'department/department.html'

class citedep(TemplateView):
    template_name = 'department/cite.html'
    
def home(request):
    obj = Course.objects.all()
    context = {'obj': obj}
    return render(request, 'home.html', context)

#BSCS
@method_decorator([login_required, teacher_required], name='dispatch')
class bscsfirst(generic.ListView):
	def get(self, request): 
		query = self.request.GET.get('q')
		students = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='1st')
		context = {'students':students,}
		return render(request, "student_list.html", context)


@method_decorator([login_required, teacher_required], name='dispatch')
class bscssecond(generic.ListView):
	def get(self, request): 
		query = self.request.GET.get('q')
		students = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='2nd')
		context = {'students':students,}
		return render(request, "student_list.html", context)

@method_decorator([login_required, teacher_required], name='dispatch')
class bscsthird(generic.ListView):
	def get(self, request): 

		query = self.request.GET.get('q')
		students = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='3rd')
		context = {'students':students,}
		return render(request, "student_list.html", context)
		
@method_decorator([login_required, teacher_required], name='dispatch')
class bscsfourth(generic.ListView):

	def get(self, request): 
		query = self.request.GET.get('q')
		students = MyUser.objects.filter(course__course_name__contains='BSCS',Year__contains='4rth')
		context = {'students':students,}
		return render(request, "student_list.html", context)

@method_decorator([login_required, teacher_required], name='dispatch')
class RegisterView(CreateView):
	model = User
	form_class = UserCreationForm
	template_name = 'forms/signup_form.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'student'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('/home')
@method_decorator([login_required, teacher_required], name='dispatch')
class FacultyRegisterView(CreateView):
	model = User
	form_class = facultyCreationForm
	template_name = 'forms/signup_form.html'


	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'faculty'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('/home')


@method_decorator([login_required, teacher_required], name='dispatch')
class StudentUpdateView(UpdateView):
	model = User
	form_class = UserCreationForm
	template_name = 'forms/update_form.html'
	

	def get_object(self):
		last_name = self.kwargs.get("last_name")
		if last_name is None:
			raise Http404
		return get_object_or_404(User, last_name__iexact=last_name, is_active=True)

	def get_context_data(self, *args, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Update student'
		return context

	#for user checking if login of not
	#giving data
	def get_form_kwargs(self):
		kwargs = super(StudentUpdateView, self).get_form_kwargs()
		return kwargs

@method_decorator([login_required, teacher_required], name='dispatch')
class FacultyUpdateView(UpdateView):
	model = User
	form_class = facultyCreationForm
	template_name = 'forms/update_form.html'
	

	def get_object(self):
		last_name = self.kwargs.get("last_name")
		if last_name is None:
			raise Http404
		return get_object_or_404(User, last_name__iexact=last_name, is_active=True)
		
	def get_context_data(self, *args, **kwargs):
		context = super(FacultyUpdateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Update faculty'
		return context

	#for user checking if login of not
	#giving data
	def get_form_kwargs(self):
		kwargs = super(FacultyUpdateView, self).get_form_kwargs()
		return kwargs