from django.db import models
from django.conf import settings
from django.db.models import Q
from django.db.models.signals import pre_save
from django.urls import reverse 
from professor.models import professor
from django.core.mail import send_mail
from .utils import unique_slug_generator
User = settings.AUTH_USER_MODEL
# Create your models here.

class subjectQuerySet(models.query.QuerySet):
    def search(self, query): 
        if query:
            query = query.strip()
            return self.filter(
                Q(subject_name__icontains=query)|
                Q(grade__quiz__icontains=query)|
                Q(grade__quiz__iexact=query)|
                Q(grade__performance__icontains=query)|
                Q(grade__performance__iexact=query)|
                Q(grade__exam__icontains=query)|
                Q(grade__exam__iexact=query)|
                Q(grade__trinal__icontains=query)|
                Q(grade__trinal__iexact=query)|
                Q(grade__midterm__icontains=query)|
                Q(grade__midterm__iexact=query)|
                Q(grade__Final__icontains=query)|
                Q(grade__Final__iexact=query)
                ).distinct()
        return self

#search
class subjectManager(models.Manager):
    def get_queryset(self):
        return subjectQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)



class subject(models.Model):

	subject_name		 = 		models.CharField(max_length=150)
	subject_Descreption  = 	 	models.CharField(max_length=200)	

	objects = subjectManager()	

	def __str__(self):
		return self.subject_name

	def get_absolute_url(self):
		return reverse('subject-detail', args=[str(self.id)])

	def get_absolute_url1(self):
		return reverse('subject', kwargs={'slug': self.slug})

	def rl_pre_save_receiver(sender, instance, *args, **kwargs):
		if not instance.slug:
			instance.slug = unique_slug_generator(instance)