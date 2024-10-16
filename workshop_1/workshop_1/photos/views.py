from django.shortcuts import render, redirect
from django.template.defaulttags import comment

from workshop_1.common.forms import CommentForm
from workshop_1.photos.forms import PhotoCreateForm, PhotoEditForm
from workshop_1.photos.models import Photo


# Create your views here.
def add_photo(request):

    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {'form': form}

    return render(request, 'photos/photo-add-page.html', context)


def show_photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    comment_form = CommentForm()
    likes = photo.like_set.all()
    comments = photo.comment_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, request.FILES or None, instance=photo)

    if form.is_valid():
        form.save()
        return redirect('show-photo', pk=pk)

    context = {'form': form}

    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home')