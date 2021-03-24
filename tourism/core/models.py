from django.db import models

from tourism.address.models import Address
from tourism.attraction.models import Attraction
from tourism.comment.models import Comment
from tourism.ratting.models import Ratting


class Document(models.Model):
    description = models.CharField('descrição', max_length=50, unique=True)

    class Meta:
        ordering = ('description',)
        verbose_name = 'documento'
        verbose_name_plural = 'documentos'

    def __str__(self):
        return self.description


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
    photo = models.ImageField(upload_to='tourist_spot', null=True, blank=True)
    document = models.OneToOneField(
        Document,
        on_delete=models.CASCADE,
        verbose_name='documento',
        related_name='documents',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'ponto turístico'
        verbose_name_plural = 'pontos turísticos'

    def __str__(self):
        return self.name

    @property
    def complete_description(self):
        return f'{self.name} - {self.description}'
