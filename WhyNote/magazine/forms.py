from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from django.forms import ModelForm

class CommentForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['post_name'].empty_label =
    text = forms.Textarea(attrs={'required': True, "placeholder": 'Добавить коментарий',
                                 'cols': 32})

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'required': True, "placeholder": 'Добавить коментарий',
                                 'cols': 32})
        }

class Add_article(ModelForm):
    title = forms.CharField(label='Название статьи', required=True, widget=forms.TextInput(
        attrs={'class': 'email_input', "placeholder": 'Введите название статьи'}))
    text = forms.Textarea(attrs={'class': 'email_input2','required': True,
                                 "placeholder": 'Текст статьи'})
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'up_photo'}))
    class Meta:
        model = article
        fields = ['title', 'text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'email_input2','required': True,
                                 "placeholder": 'Текст статьи'}),
            'photo': forms.FileInput(attrs={'class': 'up_photo'})
        }