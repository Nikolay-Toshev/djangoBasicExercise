from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from workshop_1.accounts.forms import AppUserCreationForm, AppUserLoginForm, ProfileEditForm
from workshop_1.accounts.models import Profile

UserModel = get_user_model()


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class AppUserLoginView(LoginView):
    form_class = AppUserLoginForm
    template_name = 'accounts/login-page.html'

    def form_valid(self, form):
        super().form_valid(form)
        profile_instance, _ = Profile.objects.get_or_create(user=self.request.user)
        return HttpResponseRedirect(self.get_success_url())

class AppUserLogoutView(LogoutView):
    pass

# def show_profile_details(request, pk):
#     return render(request, 'accounts/profile-details-page.html')

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'accounts/profile-details-page.html'
    def get_object(self, queryset=None):
        return self.request.user.profile


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html')