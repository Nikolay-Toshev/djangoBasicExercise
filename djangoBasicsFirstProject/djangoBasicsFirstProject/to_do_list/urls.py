from django.urls import path
from djangoBasicsFirstProject.to_do_list.views import list_of_tasks

urlpatterns = [
    path('', list_of_tasks)
]