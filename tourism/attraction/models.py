from django.db import models


class Attraction(models.Model):
    name = models.CharField('nome', max_length=100, unique=True)
    description = models.TextField('descrição', null=True, blank=True)
    opening_hours = models.TextField('funcionamento', null=True, blank=True)
    min_age = models.PositiveIntegerField('idade mínima')

    class Meta:
        ordering = ('name',)
        verbose_name = 'atração'
        verbose_name_plural = 'atrações'

    def __str__(self):
        return self.name
