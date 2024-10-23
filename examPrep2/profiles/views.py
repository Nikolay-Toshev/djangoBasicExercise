from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation.template import context_re
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from car.models import Car
from profiles.forms import ProfileCreateForm, ProfileEditForm
from profiles.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'profile/profile-create.html'
    success_url = reverse_lazy('catalogue')
    form_class = ProfileCreateForm


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile/profile-details.html'

    def get_object(self, queryset=None):
        return Profile.objects.all().first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_cars_price = 0
        for car in Car.objects.all():
            all_cars_price += car.price
        context['all_cars_price'] = all_cars_price
        return context



class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'profile/profile-edit.html'
    success_url = reverse_lazy('catalogue')
    form_class = ProfileEditForm


    def get_object(self, queryset=None):
        return Profile.objects.all().first()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return Profile.objects.all().first()