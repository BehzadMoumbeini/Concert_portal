from django import forms
from .models import Concertmodel


class SearchForm(forms.Form):
    SearchText=forms.CharField(max_length=100, label="concert name", required=False)



class ConcertForm(forms.ModelForm):
    class Meta:
        model = Concertmodel
        fields = ['Name', 'SingerName', 'Length', 'Poster']
        # exclude = ['Poster']