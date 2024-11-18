from django import forms
from account_app.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core import validators
from .managers import UserManager
from.models import OtpCode




# class UserCreationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""

#     password1 = forms.CharField(label="گذرواژه", widget=forms.PasswordInput)
#     password2 = forms.CharField(
#         label="تکرار گذرواژه", widget=forms.PasswordInput
#     )

#     class Meta:
#         model = User
#         fields = ["phone",]

#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Passwords don't match")
#         return password2

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user

class UserCreationsForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm passwod', widget=forms.PasswordInput)
    
    
    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name')
        
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('passwords no match')
        return cd['password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


# class UserChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     disabled password hash display field.
#     """

#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = User
#         fields = ["phone", "password", "is_active", "is_admin"]

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="you can change password using <a href=\"../password/\">this form</a>")
    
    class Meta:
        model = User
        fields = ('phone_number', 'email', 'full_name', 'password')
        
        

class UserResitrationForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField(label='full name')
    phone_number = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)
    
    #اعتباری سنجی ایمیل و شماره موبایل  
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('this email already exits')
        return email
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        user = User.objects.filter(phone_number = phone_number).exists()
        if user:
            raise ValidationError('this phone_number already exists')
        OtpCode.objects.filter(phone_number=phone_number).delete()
        return phone_number
    
class VeriFycodeForm(forms.Form):
    code = forms.IntegerField()
    
    
class UserLoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
class LoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    # slug = forms.SlugField() 
  
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    # def clean_phone(self):
    #     # phone = self.cleaned_data.get('phone')
    #     # if len (phone) > 11:
    #     #     raise validators('تلفن وارد شده معتبر نیست')
    #     phone = self.cleaned_data.get('phone')
    #     if len(phone) > 11 :
    #         raise validators('تلفن وارد شده معتبر نیست', code='invalid_phone')
    #     return phone
    
    
def clean(self):
    cd = super().clean()
    phone = cd['phone']
    if len (phone) > 11:
        raise ValidationError(
        ("Invalid value: %(value)s is invalid"),
         code="invalid",
         params={"value": f'{phone}'},
)
       
       
class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()