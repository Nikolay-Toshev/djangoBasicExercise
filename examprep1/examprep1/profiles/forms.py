from django import forms

from examprep1.profiles.models import Profile


class AddProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'