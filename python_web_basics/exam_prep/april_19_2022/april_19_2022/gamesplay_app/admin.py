from django.contrib import admin

from april_19_2022.gamesplay_app.models import ProfileModel, GameModel


# Register your models here.
@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    pass


@admin.register(GameModel)
class GameModelAdmin(admin.ModelAdmin):
    pass

