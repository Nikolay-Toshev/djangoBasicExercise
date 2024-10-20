from django import forms
from examprep1.albums.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'artist', 'genre', 'description', 'image_url', 'price']
        widgets = {
            'genre': forms.Select(attrs={'class': 'form-control'}),
        }


class AlbumDeleteForm(AlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
