from django.shortcuts import render

def user_login(request):
    return render(request, 'account_app/contact.html', {})
