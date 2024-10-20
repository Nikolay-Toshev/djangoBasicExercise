from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from examprep1.albums.models import Album
from examprep1.profiles.forms import AddProfileForm
from examprep1.profiles.models import Profile


def home_page(request):

    if Profile.objects.all():
        all_albums = Album.objects.filter(owner_id=Profile.objects.get().pk).all()
        context = {
            'all_albums': all_albums,
        }
        return render(request, 'profiles/home-with-profile.html', context)

    form = AddProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'profiles/home-with-profile.html')


    return render(request, 'home-no-profile.html', {'form': form, 'user': False})


def profile_details(request):
    profile = Profile.objects.get()

    return render(request, 'profiles/profile-details.html', {'profile': profile})


def profile_delete(request):

    if request.method == 'POST':
        profile = Profile.objects.get()
        profile.delete()
        return redirect('home')

    return render(request, 'profiles/profile-delete.html')


