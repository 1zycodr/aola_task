from django.contrib import admin
from feed import models


@admin.register(models.Note)
class NoteAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Achievement)
class AchievementAdmin(admin.ModelAdmin):
    pass


@admin.register(models.UserAchievement)
class UserAchievementsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    pass
