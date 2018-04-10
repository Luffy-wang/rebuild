from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from account.models import User





class UserAdmin(BaseUserAdmin):
    
    # The forms to add and change user instances
    # form = UserChangeForm
    # add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
     list_display = ('user_id', 'user_name', 'user_type')
     list_filter = ('user_type',)
    #  fieldsets = (
    #      (None, {'fields': ('user_id', 'password')}),
    #      ('Personal info', {'fields': ('user_name',)}),
    #      ('Permissions', {'fields': ('user_type',)}),
    #  )
    # # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # # overrides get_fieldsets to use this attribute when creating a user.
    #  add_fieldsets = (
    #      (None, {
    #          'classes': ('wide',),
    #          'fields': ('user_id', 'user_name', 'password1', 'password2')}
    #      ),
    #  )
     search_fields = ('user_id',)
     ordering = ('user_id',)
     filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)