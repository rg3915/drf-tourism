from django.db import models
from django.contrib.auth.models import User


class Ratting(models.Model):
    comment = models.CharField('comentário', max_length=100, unique=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='usuário',
        related_name='ratting_users',
        null=True,
        blank=True
    )
    note = models.DecimalField('nota', max_digits=3, decimal_places=2)
    created = models.DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )

    class Meta:
        ordering = ('comment',)
        verbose_name = 'avaliação'
        verbose_name_plural = 'avaliações'

    def __str__(self):
        return self.comment
