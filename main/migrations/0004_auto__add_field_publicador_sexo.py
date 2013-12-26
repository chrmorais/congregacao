# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Publicador.sexo'
        db.add_column(u'publicador', 'sexo',
                      self.gf('django.db.models.fields.CharField')(default='M', max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Publicador.sexo'
        db.delete_column(u'publicador', 'sexo')


    models = {
        u'main.congregacao': {
            'Meta': {'object_name': 'Congregacao', 'db_table': "u'congregacao'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'numero': ('django.db.models.fields.IntegerField', [], {})
        },
        u'main.grupo': {
            'Meta': {'object_name': 'Grupo', 'db_table': "u'grupo'"},
            'congregacao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Congregacao']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.publicador': {
            'Meta': {'object_name': 'Publicador', 'db_table': "u'publicador'"},
            'anciao': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'batismo': ('django.db.models.fields.DateField', [], {}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Grupo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'nascimento': ('django.db.models.fields.DateField', [], {}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pioneiro_regular': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'servo_ministerial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['main']