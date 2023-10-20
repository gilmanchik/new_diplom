from django import forms
from .models import *


class AddMusicForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория'

    class Meta:
        model = Music
        fields = ['title', 'author', 'slug', 'image', 'soundfile', 'release', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'})
        }
