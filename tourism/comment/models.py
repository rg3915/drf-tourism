from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    comment = models.CharField('comentário', max_length=100, unique=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='usuário',
        related_name='comment_users',
        null=True,
        blank=True
    )
    approved = models.BooleanField('aprovado', default=False)
    created = models.DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )

    class Meta:
        ordering = ('comment',)
        verbose_name = 'comentário'
        verbose_name_plural = 'comentários'

    def __str__(self):
        return self.comment
