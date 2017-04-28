from django import forms
from movie.choices import *
from django.contrib.auth.models import User


class signupForm(forms.Form):
    firstName = forms.CharField(max_length=100)
    lastName = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField(max_value=100, min_value=0)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select)
    profession = forms.ChoiceField(choices=PROFESSION_CHOICES, widget=forms.Select)
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, widget=forms.Select)
    username = forms.CharField(max_length=100, required=True)
    password1 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)
    image = forms.FileField()

    firstName.widget.attrs['class'] = 'tinp'
    lastName.widget.attrs['class'] = 'tinp'
    email.widget.attrs['class'] = 'tinp'
    age.widget.attrs['class'] = 'tinp'
    age.widget.attrs['id'] = 'tinp3'
    gender.widget.attrs['id'] = 'gender'
    profession.widget.attrs['id'] = 'profession'
    country.widget.attrs['id'] = 'country'
    username.widget.attrs['class'] = 'tinp'
    password1.widget.attrs['class'] = 'tinp'
    password2.widget.attrs['class'] = 'tinp'
    image.widget.attrs['class'] = 'choose_file'
    image.widget.attrs['accept'] = 'image/gif, image/jpeg, image/png'


    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        passwrod2 = self.cleaned_data['password2']
        if password1 != passwrod2:
            raise forms.ValidationError('password fields mismatch.')
        return passwrod2


    def clean_username(self):
        usr = self.cleaned_data['username']
        num = User.objects.filter(username=usr).count()
        if num > 0:
            raise forms.ValidationError('username already exists.')
        return usr


class signinForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)
    username.widget.attrs['class'] = 'ipt'
    username.widget.attrs['id'] = 'usr'
    password.widget.attrs['class'] = 'ipt'
    password.widget.attrs['id'] = 'pass'
