from django import forms
from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'



class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):

        help_texts = {
            'age': "Age requirement: 21 years and above.",
        }
        widgets = {
            'password': forms.PasswordInput(),
        }

        exclude = ['first_name', 'last_name', 'profile_picture']


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    pass