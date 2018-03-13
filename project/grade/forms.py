from django import forms
 

from .models import Grade

from django.forms import ModelForm, Textarea

class GradeCreate(forms.ModelForm):
	class Meta:
		model = Grade
		fields = [
			'user',
			'First_year_Grade',
			'Second_year_Grade',
			'Third_year_Grade',
			'Fourth_year_Grade',
			'subject',
			'professor',
			'quiz',
			'performance',
			'exam',
			'trinal',
			'midterm',
			'Final',

		]
 