from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from django.forms import ModelForm

class Add_music(ModelForm):
    avtor = forms.CharField(label='Автор песни', required=True, widget=forms.TextInput(
        attrs={'class': 'email_input', "placeholder": 'Введите автора песни'}))
    name_song = forms.CharField(label='Название песни', required=True, widget=forms.TextInput(
        attrs={'class': 'email_input', "placeholder": 'Введите название песни'}))
    feat = forms.CharField(label='Второй исполнитель', required=False, widget=forms.TextInput(
        attrs={'class': 'email_input', "placeholder": 'Введите соавтора песни'}))
    genre = forms.ModelChoiceField(queryset=Genre_songs.objects.all(), widget=forms.Select(attrs={'class': 'select_donwload'}), required=False)

    photo_song = forms.ImageField(widget=forms.FileInput(attrs={'class': 'up_photo', 'id': 'input__file2'}))
    song_path = forms.FileField(widget=forms.FileInput(attrs={'class': 'up_photo', 'id': 'input__file'}), required=True)
    class Meta:
        model = Music
        fields = ['name_song', 'avtor', 'photo_song', 'song_path', 'feat']
        widgets = {
            'avtor': forms.Textarea(attrs={'class': 'email_input2','required': True,
                                 "placeholder": 'Текст статьи'}),
            'photo': forms.FileInput(attrs={'class': 'up_photo'})
        }
