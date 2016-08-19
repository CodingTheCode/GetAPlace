# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


# Locais disponíveis para locação
class Local(models.Model):
    dono = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='locais')
    nome = models.CharField(max_length=64)
    endereco = models.TextField()
    bairro = models.CharField(max_length=64)
    cidade = models.CharField(max_length=64)
    estado = models.CharField(max_length=64)
    pais = models.CharField(max_length=64)
    atributos = models.ManyToManyField('Atributo', null=True, blank=True)


# Características de locais
class Atributo(models.Model):
    nome = models.CharField(max_length=64)


# Reviews de usuários sobre locais
class Review(models.Model):
    GOSTOS_CHOICES = (
        ('pessimo', _("Péssimo")),
        ('ruim', _("Ruim")),
        ('regular', _("Regular")),
        ('bom', _("Bom")),
        ('otimo', _("Ótimo")),
    )

    local = models.ForeignKey(Local, related_name='reviews')
    titulo = models.CharField(max_length=64)
    texto = models.TextField()
    avaliacao = models.CharField(choices=GOSTOS_CHOICES, default='regular', max_length=64)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews')
