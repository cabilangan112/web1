from django.db import models
from django.urls import reverse
# Create your models here.

class professor(models.Model):
	
	first_name		= models.CharField(max_length=150)
	last_name 		= models.CharField(max_length=150)

	
	def get_absolute_url(self):
		return reverse('professor-detail', args=[str(self.id)])
		
	def __str__(self):
		return '%s, %s' % (self.last_name, self.first_name)
		