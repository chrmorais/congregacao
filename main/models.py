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

    def __unicode__(self):
        return self.nome

class Grupo(models.Model):
    congregacao = models.ForeignKey(Congregacao, verbose_name='Congregação')
    nome = models.CharField(max_length=50)

    class Meta:
        db_table = 'grupo'

class Publicador(TimeStampedModel):
    grupo = models.ForeignKey(Grupo)
    nome = models.CharField(max_length=100)
    nome_curto = models.CharField(max_length=50)
    ESCOLHAS_SEXO = (('M', 'Masculino'), ('F', 'Feminino'),)
    sexo = models.CharField(max_length=1, choices=ESCOLHAS_SEXO)
    endereco = models.CharField(max_length=150, null=True)
    telefone = models.CharField(max_length=15, null=True)
    celular = models.CharField(max_length=15, null=True)
    nascimento = models.DateField(null=True)
    batismo = models.DateField(null=True)
    anciao = models.BooleanField(default=False)
    servo_ministerial = models.BooleanField(default=False)
    pioneiro_regular = models.BooleanField(default=False)
    ESCOLHAS_TIPO = (('E', 'Estudante'), ('P', 'Publicador'), ('D', 'Desassociado'), ('I', 'Inativo'),)
    tipo = models.CharField(max_length=1)

    class Meta:
        db_table = 'publicador'
        verbose_name_plural = 'publicadores'
