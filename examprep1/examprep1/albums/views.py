from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from examprep1.albums.forms import AlbumForm, AlbumDeleteForm
from examprep1.albums.models import Album
from examprep1.profiles.models import Profile


def add_album(request):
    form = AlbumForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        album = form.save(commit=False)
        album.owner = Profile.objects.get()
        album.save()
        return redirect(reverse_lazy('home'))

    context = {'form': form}

    return render(request, 'albums/album-add.html', context)

class AlbumDetailView(DetailView):
    model = Album
    form_class = AlbumForm()
    template_name = 'albums/album-details.html'
    pk_url_kwarg = 'id'
    context_object_name = 'album'


class AlbumEditView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/album-edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')


class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'albums/album-delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return Album.objects.get(pk=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AlbumDeleteForm(initial=self.object.__dict__)

        return context

    def delete(self, request, *args, **kwargs):
        album = self.get_object()
        album.delete()
        return redirect(self.get_success_url())


