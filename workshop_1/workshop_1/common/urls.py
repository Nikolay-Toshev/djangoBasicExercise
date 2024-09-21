from django.urls import path

from workshop_1.common.views import index

urlpatterns = [
    path('', index, name='home'),
]