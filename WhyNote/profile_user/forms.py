from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    about_me = forms.CharField(label='Расскажите о себе', required=True, widget=forms.Textarea(attrs={'class': 'email_input','required': True, "placeholder": 'Расскажите о себе'}))




    # class Meta:
    #     model = Profile
    #     fields = ('photo',)
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Придумайте логин', required=True, widget=forms.TextInput(attrs={'class': 'email_input', "placeholder": 'Придумайте Логин'}))
    email = forms.EmailField(label='Ваш адрес электронной почты',
                               widget=forms.TextInput(attrs={'class': 'email_input', "placeholder": 'Введите ваш адресс E-mail'}))
    password1 = forms.CharField(label='Пароль', error_messages={'invalid': 'Пожалуйста, введите правильный адрес электронной почты'},
                                widget=forms.PasswordInput(attrs={'class': 'email_input', "placeholder": 'Придумайте пароль'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'email_input', "placeholder": 'Повторите пароль'}))
    first_name = forms.CharField(label='Ваше имя', required=True, widget=forms.TextInput(attrs={'class': 'email_input', "placeholder": 'Как вас зовут?'}))
    class Meta:
        model = User
        fields = ['username', "email", 'password1', 'password2', 'first_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'email_input'}),
            'email': forms.TextInput(attrs={'class': 'email_input'}),
            'password1': forms.PasswordInput(attrs={'class': 'email_input'}),
            'password2': forms.PasswordInput(attrs={'class': 'email_input'}),
            'first_name': forms.TextInput(attrs={'class': 'email_input'}),

        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def clean_password(self):
        if self.data['password1'] != self.data['password2']:
            self.add_error('password1', "Эта почта уже зарегестрированна")

            raise forms.ValidationError('Passwords are not the same')
        return self.data['password1']

    def clean(self):
        print(self)
        cleaned_data = super().clean()
        print(cleaned_data)
        if User.objects.filter(email=cleaned_data.get('email')).exists():
            self.add_error('email', "Эта почта уже зарегестрированна")
        return cleaned_data

class LodinUserForm(AuthenticationForm):
    username = forms.CharField(label='Введите логин', required=True, widget=forms.TextInput(attrs={'class': 'email_input', "placeholder": 'Введите логин'}))

    password = forms.CharField(label='Пароль',
                                error_messages={'invalid': 'Пожалуйста, введите правильный адрес электронной почты'},
                                widget=forms.PasswordInput(
                                    attrs={'class': 'email_input', "placeholder": 'Введите пароль'}))