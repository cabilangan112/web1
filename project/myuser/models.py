from django.urls import reverse
from django.db import models
from course.models import Course
from .utils import unique_slug_generator
from django.db.models import Q
from django.contrib.auth.models import (
     BaseUserManager, AbstractBaseUser
)
class userQuerySet(models.query.QuerySet):
    def search(self, query): 
        if query:
            query = query.strip()
            return self.filter(

                Q(grade__quiz__contains=query)|
                Q(grade__quiz__exact=query)|
                Q(grade__performance__contains=query)|
                Q(grade__performance__exact=query)|
                Q(grade__exam__contains=query)|
                Q(grade__exam__exact=query)|
                Q(grade__trinal__contains=query)|
                Q(grade__trinal__exact=query)|
                Q(grade__midterm__contains=query)|
                Q(grade__midterm__exact=query)|
                Q(grade__Final__contains=query)|
                Q(grade__Final__exact=query)
                ).distinct()
        return self

#search
class userManager(models.Manager):
    def get_queryset(self):
        return userQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
 
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    Student_profile =   models.ImageField(upload_to = 'static/media')
    last_name      =    models.CharField(max_length=100)
    first_name     =   models.CharField(max_length=100)
    MI             =   models.CharField(max_length=200)
    Gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    Sex             =   models.CharField(max_length=6, choices=Gender, blank=True, default=True)
    date_of_birth   =   models.DateField()
    Age             =   models.CharField(max_length=20)
    course          =   models.ForeignKey(Course,on_delete=models.SET_NULL, null=True)
    years = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4rth', '4rth'),
    )
    Year            = models.CharField(max_length=6, choices=years, blank=True, default=True)

    objects         = MyUserManager()
    is_active       = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)
    is_faculty      = models.BooleanField(default=False)
    is_student      = models.BooleanField(default=False)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return '%s, %s, %s, %s'  % (self.last_name, self.first_name, self.course, self.Year)

    def get_absolute_url(self):
        return u'/some_url/%d' % self.id 
        
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin