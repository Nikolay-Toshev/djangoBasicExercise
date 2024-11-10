
from django.urls import path, include

from workshop_1.accounts.views import delete_profile, \
    AppUserRegisterView, AppUserLoginView, AppUserLogoutView, ProfileEditView, ProfileDetailView

urlpatterns = [
    path('register/', AppUserRegisterView.as_view(), name='register'),
    path('login/', AppUserLoginView.as_view(), name='login'),
    path('logout/', AppUserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', include([
        path('', ProfileDetailView.as_view(), name='profile-details'),
        path('edit/', ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', delete_profile, name='profile-delete'),

    ]))

]