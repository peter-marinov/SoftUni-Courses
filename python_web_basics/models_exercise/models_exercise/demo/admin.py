from django.contrib import admin
from models_exercise.demo.models import People, Cities
# Register your models here.


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'age')


@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    pass
