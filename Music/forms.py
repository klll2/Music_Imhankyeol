from django import forms
from Music.models import Music

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = '__all__'

