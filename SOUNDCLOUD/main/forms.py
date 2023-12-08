from django import forms
from .models import *


class AddMusicForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория'

    class Meta:
        model = Music
        fields = ['title', 'author', 'image', 'soundfile', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'})
        }

    def clean_soundfile(self):
        cd = str(self.cleaned_data['soundfile'])
        mp3 = cd.split('.')
        if mp3[-1] != 'mp3':
            raise forms.ValidationError('Неверный формат аудиофайла')
