from django import forms

from car.models import Car


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']

class CarCreateForm(CarBaseForm):
    class Meta(CarBaseForm.Meta):
        widgets = {
            'image_url': forms.TextInput(attrs={'placeholder': 'https://...'}),
        }


class EditCarForm(CarBaseForm):
    pass


class DeleteCarForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
