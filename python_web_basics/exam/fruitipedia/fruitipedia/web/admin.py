from django.contrib import admin

from fruitipedia.web.models import ProfileModel, FruitModel


# Register your models here.
@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    pass


@admin.register(FruitModel)
class FruitModelAdmin(admin.ModelAdmin):
    pass
