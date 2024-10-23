from django.urls import path

from profiles.views import ProfileCreateView, ProfileDetailView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='profile_create'),
    path('details/', ProfileDetailView.as_view(), name='profile_detail'),
    path('edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('delete/', ProfileDeleteView.as_view(), name='profile_delete'),
]