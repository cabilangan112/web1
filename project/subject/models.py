from django.db import models
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.urls import reverse 
from django.core.mail import send_mail
# Create your models here.


class subject(models.Model):

	subject_name		 = 		models.CharField(max_length=150)
	subject_Descreption  = 	 	models.CharField(max_length=200)	

	

	def __str__(self):
		return self.subject_name

	def get_absolute_url(self):
		return reverse('subject-detail', args=[str(self.id)])

	def get_absolute_url1(self):
		return reverse('subject', kwargs={'slug': self.slug})

	def rl_pre_save_receiver(sender, instance, *args, **kwargs):
		if not instance.slug:
			instance.slug = unique_slug_generator(instance)