from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from .models import professor
from  myuser.models import MyUser
class TeacherSignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('email',
         'Student_profile',
         'last_name',
         'first_name',
         'MI',
         'Sex',
         'date_of_birth',
         'Age',
         'is_faculty',
         'is_student')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_faculty= True
        user.save()
        professor = professor.objects.create(user=user)

        return user
