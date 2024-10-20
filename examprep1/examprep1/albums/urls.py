from django.urls import path, include
from examprep1.albums.views import add_album, AlbumDetailView, AlbumEditView, AlbumDeleteView

urlpatterns = [
    path('add/', add_album, name='add_album'),
    path('<int:id>/', include([
        path('edit/', AlbumEditView.as_view(), name='edit_album'),
        path('delete/', AlbumDeleteView.as_view(), name='delete_album'),
        path('details/', AlbumDetailView.as_view(), name='album_detail'),
    ])),
]