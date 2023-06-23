from django.contrib import admin

from dec_21_2022.web.models import Profile, Plant


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name']


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ['plant_type', 'name']

