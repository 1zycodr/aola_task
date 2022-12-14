from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Note, Event, UserAchievement, Advertisement


@receiver(post_save, sender=Note)
def create_note_event(sender, instance: Note, created, **kwargs):
    if created:
        Event.objects.create(
            user=instance.creator,
            kind=Event.Type.NOTE,
            note=instance,
        )


@receiver(post_save, sender=UserAchievement)
def create_achieve_event(sender, instance: UserAchievement, created, **kwargs):
    if created:
        Event.objects.create(
            user=instance.user,
            kind=Event.Type.ACHIEVEMENT,
            achievement=instance.achievement,
        )


@receiver(post_save, sender=Advertisement)
def create_advertisement_event(sender, instance: Advertisement, created, **kwargs):
    if created:
        Event.objects.create(
            kind=Event.Type.ADVERTISEMENT,
            advertisement=instance,
        )
