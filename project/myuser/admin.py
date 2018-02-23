from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm,UserCreationForm
from .models import MyUser 


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('last_name','first_name','email', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (

        ('information', {'fields': ('Student_profile','last_name','first_name','MI','Sex','Age','course','Year',)}),
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin','Faculty','Student')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('last_name','first_name','email', 'date_of_birth', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)

# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
