from django import forms
from .models import Album
from datetime import datetime

class AlbumForm(forms.ModelForm):
    class Meta:
        model=Album
        fields='__all__'

        labels={
            'album_name':'Album Name',
            'album_release_date':'Release Date',
            'rating':'Rating',
            'author':'Author'
        }

        help_texts={
            'album_name':'Enter Album Name',
            'album_release_date':'Enter Release Date',
            'rating':'Enter Rating',
            'author':'Enter Author'
        }
        widgets = {
            'album_release_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
        

        
    


        
        





