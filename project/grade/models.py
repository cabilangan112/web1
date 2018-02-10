from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.urls import reverse 
from django.core.mail import send_mail
from subject.models import subject
from course.models import Course
from professor.models import professor
user = settings.AUTH_USER_MODEL
from subject.utils import unique_slug_generator
from professor.utils import unique_slug_generator
from user.utils import unique_slug_generator

# Create your models here.



class Grade(models.Model):
	user		 =      models.ForeignKey(user,on_delete=models.SET_NULL, null=True)
	course 		 =      models.ForeignKey(Course,on_delete=models.SET_NULL, null=True)
	subject 	 =      models.ForeignKey(subject,on_delete=models.SET_NULL, null=True)
	professor 	 =      models.ForeignKey(professor,on_delete=models.SET_NULL, null=True)
	quiz		 = 		models.IntegerField(null=True)
	performance	 =	    models.IntegerField(null=True)
	exam         =      models.IntegerField(null=True)

	trinal		 = 		models.BooleanField(default=False)
	midterm      =      models.BooleanField(default=False)
	Final        =      models.BooleanField(default=False)

	

	def get_computed(self):
		result = self.quiz * 0.25 + self.performance * 0.25 + self.exam  * 0.50 
		return result

	def save(self, *args, **kwargs):
		self.computed = self.get_computed()
		super(Grade, self).save(*args, **kwargs)
	

	def __str__(self):
		return '%s, %s' % (self.user.last_name, self.user.first_name)
	
	def get_absolute_url(self):
		return reverse('grade-detail', args=[str(self.id)])

	def get_absolute_url1(self):
		return reverse('grade', kwargs={'slug': self.slug})

	def rl_pre_save_receiver(sender, instance, *args, **kwargs):
		if not instance.slug:
			instance.slug = unique_slug_generator(instance)