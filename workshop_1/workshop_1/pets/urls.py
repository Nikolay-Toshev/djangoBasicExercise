from django.urls import path, include
from workshop_1.pets.views import AddPetView, PetDetailView, PetEditView, PetDeleteView

urlpatterns = [
    path('add/', AddPetView.as_view(), name='pet-add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', PetDetailView.as_view(), name='pet-details'),
        path('edit/', PetEditView.as_view(), name='pet-edit'),
        path('delete/', PetDeleteView.as_view(), name='pet-delete'),
    ]))
]