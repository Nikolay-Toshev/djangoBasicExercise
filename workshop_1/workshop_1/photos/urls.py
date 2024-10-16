from django.urls import path, include
from workshop_1.photos.views import add_photo, show_photo_details, edit_photo, delete_photo

urlpatterns = [
    path('add/', add_photo, name='add-photo'),
    path('<int:pk>/', include([
        path('', show_photo_details, name='show-photo'),
        path('edit/', edit_photo, name='edit-photo'),
        path('delete/', delete_photo, name='delete-photo'),
    ])),
]