from django.db import models
from django.contrib.auth.models import User

from feed.mixin import TimestampMixin


class Note(TimestampMixin):

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    body = models.CharField(max_length=255, verbose_name='Тело')
    creator = models.ForeignKey(User, models.CASCADE,
                                related_name='notes', verbose_name='Создатель')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.title


class Achievement(TimestampMixin):

    name = models.CharField(max_length=100, verbose_name='Наименование')
    conditions = models.CharField(max_length=255, verbose_name='Условие получения', null=True, blank=True)
    icon = models.ImageField(upload_to='images', verbose_name='Иконка', null=True, blank=True)

    users = models.ManyToManyField(User, verbose_name='Пользователи',
                                   blank=True, through='UserAchievement')

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'

    def __str__(self):
        return self.name


class UserAchievement(TimestampMixin):

    user = models.ForeignKey(User, models.CASCADE, verbose_name='Пользователь')
    achievement = models.ForeignKey(Achievement, models.CASCADE, verbose_name='Достижение')

    class Meta:
        verbose_name = 'Достижения пользователя'
        verbose_name_plural = 'Достижения пользователей'


class Advertisement(TimestampMixin):

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.CharField(max_length=255, verbose_name='Описание')
    image = models.ImageField(upload_to='images', verbose_name='Изображение', null=True, blank=True)
    link = models.URLField(verbose_name='Ссылка на ресурс')

    class Meta:
        verbose_name = 'Рекламное объявление'
        verbose_name_plural = 'Рекламные объявления'

    def __str__(self):
        return self.title


class Event(TimestampMixin):

    class Type(models.TextChoices):
        NOTE = 'note', 'Создание заметки'
        ACHIEVEMENT = 'achieve', 'Создание достижения'
        ADVERTISEMENT = 'ad', 'Рекламное объявление'

    kind = models.CharField(max_length=10, choices=Type.choices, verbose_name='Тип')

    user = models.ForeignKey(User, models.CASCADE, 'events', null=True, blank=True, verbose_name='Пользователь')
    note = models.ForeignKey(Note, models.CASCADE, 'events', null=True, blank=True, verbose_name='Заметка')
    achievement = models.ForeignKey(Achievement, models.CASCADE, 'events',
                                    null=True, blank=True, verbose_name='Достижение')
    advertisement = models.ForeignKey(Advertisement, models.CASCADE, 'events',
                                      null=True, blank=True, verbose_name='Рекламное объявление')

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['-created_at']
