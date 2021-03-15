from django.db import models
from localflavor.br.br_states import STATE_CHOICES


class Address(models.Model):
    address = models.CharField(
        'endereço',
        max_length=100,
        null=True,
        blank=True
    )
    address_number = models.IntegerField('número', null=True, blank=True)
    complement = models.CharField(
        'complemento',
        max_length=100,
        null=True,
        blank=True
    )
    district = models.CharField(
        'bairro',
        max_length=100,
        null=True,
        blank=True
    )
    city = models.CharField('cidade', max_length=100, null=True, blank=True)
    uf = models.CharField(
        'UF',
        max_length=2,
        choices=STATE_CHOICES,
        null=True,
        blank=True
    )
    cep = models.CharField('CEP', max_length=9, null=True, blank=True)
    country = models.CharField(
        'país',
        max_length=50,
        default='Brasil',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('address',)
        verbose_name = 'endereço'
        verbose_name_plural = 'endereços'

    def __str__(self):
        return self.address
