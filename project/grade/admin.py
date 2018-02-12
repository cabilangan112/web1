from django.contrib import admin

# Register your models here.
from .models import Grade

class GradeAdmin(admin.ModelAdmin):
	list_display = ( 'user','quiz', 'performance', 'exam', 'get_computed' )

admin.site.register(Grade,GradeAdmin)
