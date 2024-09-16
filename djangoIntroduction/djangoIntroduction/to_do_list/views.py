from django.shortcuts import render

from djangoIntroduction.to_do_list.models import Todo


# Create your views here.
def list_of_tasks(request):
    data = Todo.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'to_do_list/list.html', context)