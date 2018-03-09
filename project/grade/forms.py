from django import forms
 

from .models import Grade

from django.forms import ModelForm, Textarea

class GradeCreate(forms.ModelForm):
	class Meta:
		model = Grade
		fields = [
			'user',
			'subject',
			'professor',
			'quiz',
			'performance',
			'exam',
			'trinal',
			'midterm',
			'Final',

		]
		
