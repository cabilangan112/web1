from django.db import models

# Create your models here.
class Grade(models.Model):
	Subject		 = 	 	models.ForeignKey('subject', on_delete=models.SET_NULL, null=True)
	quiz		 = 		models.IntegerField(null=True)
	performance	 =	    models.IntegerField(null=True)
	exam         =      models.IntegerField(null=True)

	Mark = models.CharField(max_length=1, choices=mark, blank=True, default='Fail')
	

	def get_computed(self):
		result = self.quiz * 0.25 + self.performance * 0.25 + self.exam  * 0.50 
		return result

	def save(self, *args, **kwargs):
		self.computed = self.get_computed()
		super(Grade, self).save(*args, **kwargs)
	
	def __str__(self):
		return self.Mark
	
	def get_absolute_url(self):
		return reverse('subject-detail', args=[str(self.id)])