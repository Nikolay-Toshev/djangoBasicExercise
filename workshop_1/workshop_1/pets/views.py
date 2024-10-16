from django.shortcuts import render, redirect

from workshop_1.common.forms import CommentForm
from workshop_1.pets.forms import PetForm, PetDeleteForm
from workshop_1.pets.models import Pet


# Create your views here.

def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)

    context = {'form': form}

    return render(request, 'pets/pet-add-page.html', context)

def show_pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()

    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form,
    }
    return render(request, 'pets/pet-details-page.html' , context)


def edit_pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet.slug)
    return render(request, 'pets/pet-edit-page.html', {'form': form})


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)

    form = PetDeleteForm(initial=pet.__dict__)
    context = {'form': form}

    return render(request, 'pets/pet-delete-page.html', context)