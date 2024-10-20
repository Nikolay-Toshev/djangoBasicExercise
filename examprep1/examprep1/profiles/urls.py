from django.urls import path, include

from examprep1.profiles.views import home_page, profile_details, profile_delete

urlpatterns = [
    path('', home_page, name='home'),
    path('profile/', include([
        path('details/', profile_details, name='profile-details'),
        path('delete/', profile_delete, name='profile-delete'),
    ])),
]

