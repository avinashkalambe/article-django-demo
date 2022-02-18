from django import forms
from django.forms import PasswordInput, ValidationError
from django.contrib.auth import get_user_model #new thing to get user model
# from django.contrib.auth.models import User   # to get the table User 


initials_tuple = (
("1","Mr"),
("2", "Mrs"),
("3","Ms")
)

class RegisterForm(forms.Form):
    initials = forms.ChoiceField(choices=initials_tuple)
    username = forms.CharField(label= 'Username' )
    password = forms.CharField(widget = forms.PasswordInput())
    confirm_password = forms.CharField(widget= forms.PasswordInput())
    email = forms.EmailField()


    def clean(self):
        print("in clean method")
        c_password = self.cleaned_data.get('password')
        c_confirm_password = self.cleaned_data.get('confirm_password')
        
        if (c_password == c_confirm_password):
            print('Both passwords are matching')
        else:
            raise ValidationError('passwords are not matching')


    def clean_username(self):
        print('to validate just username field')
        c_username = self.cleaned_data.get('username')
        User = get_user_model()
        query_string = User.objects.filter(username__iexact = c_username)

        if query_string.exists():
            raise ValidationError('Please use different username.. username already exists')
        
        return c_username


    def clean_email(self):
        print('to validate just email field')
        c_email = self.cleaned_data.get('email')
        User = get_user_model()
        query_string = User.objects.filter(email__iexact = c_email)

        if query_string.exists():
            raise ValidationError('Please use different email.. email already exists')
        
        return c_email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=PasswordInput())
    