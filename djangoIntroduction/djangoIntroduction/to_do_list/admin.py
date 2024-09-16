from django.contrib import admin
from djangoIntroduction.to_do_list.models import Todo


# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
