
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation.template import context_re
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from car.forms import CarCreateForm, EditCarForm, DeleteCarForm
from car.models import Car
from profiles.models import Profile


class CatalogueView(ListView):
    template_name = 'car/catalogue.html'
    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_cars = Car.objects.all()
        context['all_cars'] = all_cars
        return context


class CreateCarView(CreateView):
    model = Car
    template_name = 'car/car-create.html'
    success_url = reverse_lazy('catalogue')
    form_class = CarCreateForm

    def form_valid(self, form):
        form.instance.owner = Profile.objects.all().first()
        return super().form_valid(form)


class DetailsCarView(DetailView):
    model = Car
    template_name = 'car/car-details.html'
    pk_url_kwarg = 'id'


class EditCarView(UpdateView):
    model = Car
    template_name = 'car/car-edit.html'
    pk_url_kwarg = 'id'
    form_class = EditCarForm
    success_url = reverse_lazy('catalogue')


class DeleteCarView(DeleteView):
    model = Car
    template_name = 'car/car-delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('catalogue')

    def get_object(self, queryset=None):
        return Car.objects.get(id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DeleteCarForm(initial=self.object.__dict__)
        return context

    def delete(self, request, *args, **kwargs):
        car = self.get_object()
        car.delete()
        return redirect(self.get_success_url())