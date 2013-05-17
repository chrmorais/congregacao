from django.db import models

from model_utils.models import TimeStampedModel

class Grupo(models.Model):
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
