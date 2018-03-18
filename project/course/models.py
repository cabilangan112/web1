from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.urls import reverse 
from django.core.mail import send_mail
from subject.utils import unique_slug_generator
from professor.utils import unique_slug_generator

# Create your models here.


class Course(models.Model):
	
	course_name  	=  models.CharField(max_length=100)
	description 	=  models.TextField(max_length=500)
	Department	 =     models.ForeignKey('department' ,on_delete=models.SET_NULL, null=True)
	

	def __str__(self):
		return '%s' % (self.course_name  )
 
		
	def list_subjects(self):
		return ",".join([subject.subject_name for subject in self.subject.all()])

	def save(self, *args, **kwargs):
		super(Course, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('course-detail', args=[str(self.id)])

	def get_absolute_url1(self):
		return reverse('grade', kwargs={'slug': self.slug})


class department(models.Model):
	Department_name  	=  models.CharField(max_length=100)
	description 	=  models.TextField(max_length=500)


	def __str__(self):
		return self.Department_name
	