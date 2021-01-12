from django import forms
from moviechooser.library.models import Genre


class MovieChoiceForm(forms.Form):

    GENRES = [
        ('', '')
    ]

    genre = forms.ChoiceField(choices=GENRES, widget=forms.RadioSelect)