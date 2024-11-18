from django.urls import path
from .import views

app_name = "account_app"
urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('register/', views.UserRegisterView.as_view(), name='user_regester'),
    path('verify/', views.UserRigesterVeriyfyCodeView.as_view(), name='verify_code')
]