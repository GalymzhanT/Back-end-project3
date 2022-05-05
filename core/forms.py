from random import choices
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


genderChoice =(
    ("male", "Male"),
    ("female", "Female"),   
)
# Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    birthday = forms.DateField()
    bio = forms.CharField(required=False)
    phone_number = forms.CharField(required=False)
    gender = forms.ChoiceField(choices = genderChoice)

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'gender', 
            'phone_number',
            'birthday', 
            'bio', 
            'password1', 
            'password2', 
            ]


# Profile Form
class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name', 
            'last_name', 
            'email',
           # 'gender', 
           #'birthday',
           # 'bio', 
            ]
