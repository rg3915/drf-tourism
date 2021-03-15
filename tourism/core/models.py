from django.db import models
from tourism.attraction.models import Attraction
from tourism.comment.models import Comment
from tourism.ratting.models import Ratting
from tourism.address.models import Address


class TouristSpot(models.Model):
    name = models.CharField('nome', max_length=100, unique=True)
    description = models.TextField('descrição', null=True, blank=True)
    approved = models.BooleanField('aprovado', default=False)
    attractions = models.ManyToManyField(
        Attraction,
        verbose_name='atrações',
        blank=True
    )
    comments = models.ManyToManyField(
        Comment,
        verbose_name='comentários',
        blank=True
    )
    rattings = models.ManyToManyField(
        Ratting,
        verbose_name='avaliações',
        blank=True
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        verbose_name='endereço',
        related_name='adresses',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'ponto turístico'
        verbose_name_plural = 'pontos turísticos'

    def __str__(self):
        return self.name
