from django.contrib import admin
from djangoBasicsFirstProject.to_do_list.models import Todo


# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass