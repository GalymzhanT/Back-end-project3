from django.shortcuts import render
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from core.forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings



def Index(request):
    return render(request, 'htmlcov/index.html',{}) 

# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'commons/signup.html'

# Edit Profile View
class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'commons/profile.html'
    
# Lab5    send  message email
def sendanemail(request):
   
    if request.method =='POST':
        to = request.POST.get('toemail')
        content = request.POST.get('content')
        
        send_mail(
            "testing",
            content,
            settings.EMAIL_HOST_USER,
            [to],
            fail_silently = False      
        )
        
        print(to, content)  
        
        return render(
            request,
            'email.html',
            {
                'title':'send an email'
            }
        )
        
    else:
        return render(
            request,
            'email.html',
            {
                'title':'send an email'
            }
        )
        
        