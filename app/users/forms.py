from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from users.models import User
from django_recaptcha.fields import ReCaptchaField



class UserLoginForm(AuthenticationForm):

    username = forms.CharField()
    password = forms.CharField()
    
    class Meta:
        model = User
        fields=['username', 'password']


class UserRegistrationForm(UserCreationForm):
    captcha = ReCaptchaField()
    class Meta:
        model = User 
        fields=("first_name",
                "last_name",
                "username",
                "email",
                "password1",
                "password2",)
        first_name=forms.CharField()
        last_name=forms.CharField()
        username=forms.CharField()
        email=forms.CharField()
        password1=forms.CharField()
        password2=forms.CharField()
        
        


class ProfileUser(UserChangeForm):
    class Meta:
        model = User
        fields = ('image', 'first_name', 'last_name', 'username', 'email')
        
        