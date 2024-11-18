
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from .managers import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings
from django.db import models
from django.contrib.sessions.models import Session

# class UserManager(BaseUserManager):
    
#     def create_user(self,  phone_number, email, full_name, password):
#         if not phone_number:
#             raise ValueError('you must have phone_number')
        
#         if not email:
#             raise ValueError('you must have email') 
        
#         if not full_name:
#             raise ValueError('you must have full_name')
        
#         user = self.model(phone_number=phone_number, email=self.normalize_email(email), full_name=full_name)  #منظور مدل یوزر است ارث بری بکن
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
    
    
#     def create_superuser(self,  phone_number, email, full_name, password):
        
#         user = self.create_user(phone_number, email, full_name, password)
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
        
        
        


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, default=True)
        
    
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['email', 'full_name']

    def __str__(self):
        return self.phone_number

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
    
# class OtpCode(models.Model):
#     phone_number = models.CharField(max_length=11, unique=True)
#     code = models.PositiveSmallIntegerField()
#     created = models.DateTimeField(auto_now=True)
    
    
#     def __str__(self):
#         return f'{self.phone_number} - {self.code} - {self.created}'


class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.created}'
    
    
class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, unique=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)  
