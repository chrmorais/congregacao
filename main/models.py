# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from model_utils.models import TimeStampedModel

class Congregacao(models.Model):
    numero = models.IntegerField()
    nome = models.CharField(max_length=70)

    class Meta:
        db_table = 'congregacao'
        verbose_name = 'congregação'
        verbose_name_plural = 'congregações'

class Grupo(models.Model):
    congregacao = models.ForeignKey(Congregacao)
    nome = models.CharField(max_length=50)

    class Meta:
        db_table = 'grupo'

class Publicador(TimeStampedModel):
    grupo = models.ForeignKey(Grupo)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=150)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    nascimento = models.DateField()
    batismo = models.DateField()
    anciao = models.BooleanField(default=False)
    servo_ministerial = models.BooleanField(default=False)
    pioneiro_regular = models.BooleanField(default=False)

    class Meta:
        db_table = 'publicador'
        verbose_name_plural = 'publicadores'
