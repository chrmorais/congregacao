# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Publicador.nome_curto'
        db.add_column(u'publicador', 'nome_curto',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Publicador.tipo'
        db.add_column(u'publicador', 'tipo',
                      self.gf('django.db.models.fields.CharField')(default='P', max_length=1),
                      keep_default=False)


        # Changing field 'Publicador.batismo'
        db.alter_column(u'publicador', 'batismo', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Publicador.nascimento'
        db.alter_column(u'publicador', 'nascimento', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Publicador.celular'
        db.alter_column(u'publicador', 'celular', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'Publicador.telefone'
        db.alter_column(u'publicador', 'telefone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'Publicador.endereco'
        db.alter_column(u'publicador', 'endereco', self.gf('django.db.models.fields.CharField')(max_length=150, null=True))

    def backwards(self, orm):
        # Deleting field 'Publicador.nome_curto'
        db.delete_column(u'publicador', 'nome_curto')

        # Deleting field 'Publicador.tipo'
        db.delete_column(u'publicador', 'tipo')


        # User chose to not deal with backwards NULL issues for 'Publicador.batismo'
        raise RuntimeError("Cannot reverse this migration. 'Publicador.batismo' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Publicador.batismo'
        db.alter_column(u'publicador', 'batismo', self.gf('django.db.models.fields.DateField')())

        # User chose to not deal with backwards NULL issues for 'Publicador.nascimento'
        raise RuntimeError("Cannot reverse this migration. 'Publicador.nascimento' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Publicador.nascimento'
        db.alter_column(u'publicador', 'nascimento', self.gf('django.db.models.fields.DateField')())

        # User chose to not deal with backwards NULL issues for 'Publicador.celular'
        raise RuntimeError("Cannot reverse this migration. 'Publicador.celular' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Publicador.celular'
        db.alter_column(u'publicador', 'celular', self.gf('django.db.models.fields.CharField')(max_length=15))

        # User chose to not deal with backwards NULL issues for 'Publicador.telefone'
        raise RuntimeError("Cannot reverse this migration. 'Publicador.telefone' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Publicador.telefone'
        db.alter_column(u'publicador', 'telefone', self.gf('django.db.models.fields.CharField')(max_length=15))

        # User chose to not deal with backwards NULL issues for 'Publicador.endereco'
        raise RuntimeError("Cannot reverse this migration. 'Publicador.endereco' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Publicador.endereco'
        db.alter_column(u'publicador', 'endereco', self.gf('django.db.models.fields.CharField')(max_length=150))

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
            'batismo': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Grupo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'nascimento': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nome_curto': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pioneiro_regular': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'servo_ministerial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['main']