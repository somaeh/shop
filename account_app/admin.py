from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .forms import UserCreationsForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm,  UserCreationsForm
from .models import User, OtpCode,  UserSession
from django.contrib.auth.models import Group

from account_app.models import User
from django.contrib.auth.models import PermissionsMixin




# class UserAdmin(admin.ModelAdmin):
#     # The forms to add and change user instances
#     form = UserChangeForm
#     add_form = UserCreationForm

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ["phone", "is_admin"]
#     list_filter = ["is_admin"]
#     fieldsets = [
#         (None, {"fields": ["email", "password"]}),
#         ("Personal info", {"fields": ["fullname"]}),
#         ("Permissions", {"fields": ["is_admin"]}),
#     ]
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = [
#         (
#             None,
#             {
#                 "classes": ["wide"],
#                 "fields": ["email", "fullname", "password1", "password2"],
#             },
#         ),
#     ]
#     search_fields = ["email"]
#     ordering = ["email"]
#     filter_horizontal = []
    
    #=====================================================================================================
    
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationsForm
    
    
    list_display = ('full_name', 'phone_number', 'is_admin')
    list_filter = ('is_admin', )
    
    
    
    fieldsets = (
        (None, {'fields':('email', 'phone_number', 'full_name', 'password')}),
        # ('permissions', {'fields':('is_active', 'is_admin','is_superuser', 'groups', 'user_permissions')}),
    )
    
    
    add_fieldsets = (
        
        (None, {'fields':('phone_number', 'email', 'full_name', 'password1', 'password2')}),
        
    )
    
    
    search_fields = ('email', 'full_name')
    
    ordering = ('full_name', )
    
    filter_horizontal = ()
    #======================================================================================================


# Now register the new UserAdmin...
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.

# Register your models here.
admin.site.register(OtpCode)
admin.site.register( UserSession)
