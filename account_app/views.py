from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from account_app.forms import UserResitrationForm

from .forms import LoginForm, VeriFycodeForm
import random
from util import send_otp_code
from .models import OtpCode
from django.contrib import messages
from .models import User
from django.contrib.sessions.models import Session
from .models import  UserSession
class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account_app/login.html', {'form': form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                form.add_error("phone", 'invalid user data')
        else:
            form.add_error("phone", "invalid data")
            return render(request, 'account_app/login.html', {'form':form})

class UserRegisterView(View):
    
    
    form_class = UserResitrationForm
    def get(self, request):
        # if request.user.is_authenticated:
        #     return redirect('home_app:home')
    
        form = self.form_class
        return render(request, 'account_app/register.html', {'form':form})
        
       
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone_number'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'], code=random_code)
            request.session['user_registeration_info'] = {
                'phone_number': form.cleaned_data['phone_number'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password'],
                
            }
            messages.success(request, 'we send you a code', extra_tags='success')
            return redirect('account_app:verify_code')
        return redirect('home_app:home')
        
class UserRigesterVeriyfyCodeView(View):
    form_class = VeriFycodeForm
    def get(self, request):
        form = self.form_class
        return render(request, 'account_app/verify.html', {'form': form})
        
        
    def post(self, request):
        user_session = request.session['user_registeration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(user_session['phone_number'], user_session['email'], user_session['full_name'], user_session['password'])
                code_instance.delete()
                messages.success(request, 'ok register', extra_tags='success')
                return redirect('home_app:home')
            else:
                messages.error(request, 'this code is wromg', extra_tags='danger')
                return redirect('account_app:verify_code')
            return redirect('home_app:home')
                
                
       
     