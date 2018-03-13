from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.urls import reverse 
from professor.models import professor
from django.core.mail import send_mail
from .utils import unique_slug_generator
User = settings.AUTH_USER_MODEL
from myuser.models import MyUser
from django.utils.html import escape, mark_safe
# Create your models here.



class subject(models.Model):

	subject_name		 = 		models.CharField(max_length=150)
	subject_Descreption  = 	 	models.CharField(max_length=200)	
	color = models.CharField(max_length=7, default='#007bff')

	def __str__(self):
		return self.subject_name

	def get_html_badge(self):
		subject_name = escape(self.subject_name)
		subject_Descreption = escape(self.subject_Descreption)
		color = escape(self.color)
		html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
		return mark_safe(html)



	def get_absolute_url(self):
		return reverse('subject-detail', args=[str(self.id)])

	def get_absolute_url1(self):
		return reverse('subject', kwargs={'slug': self.slug})

	def rl_pre_save_receiver(sender, instance, *args, **kwargs):
		if not instance.slug:
			instance.slug = unique_slug_generator(instance)