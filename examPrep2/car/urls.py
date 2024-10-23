from django.urls import path, include

from car.views import CatalogueView, CreateCarView, DetailsCarView, EditCarView, DeleteCarView

urlpatterns = [
    path('catalogue/', CatalogueView.as_view(), name='catalogue' ),
    path('create/', CreateCarView.as_view(), name='create' ),
    path('<int:id>/', include([
        path('details', DetailsCarView.as_view(), name='details' ),
        path('edit/', EditCarView.as_view(), name='edit' ),
        path('delete/', DeleteCarView.as_view(), name='delete' ),
    ])),


]