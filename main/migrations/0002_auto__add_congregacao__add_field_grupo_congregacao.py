# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Congregacao'
        db.create_table(u'main_congregacao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal(u'main', ['Congregacao'])

        # Adding field 'Grupo.congregacao'
        db.add_column('grupo', 'congregacao',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['main.Congregacao']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Congregacao'
        db.delete_table(u'main_congregacao')

        # Deleting field 'Grupo.congregacao'
        db.delete_column('grupo', 'congregacao_id')


    models = {
        u'main.congregacao': {
            'Meta': {'object_name': 'Congregacao'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'numero': ('django.db.models.fields.IntegerField', [], {})
        },
        u'main.grupo': {
            'Meta': {'object_name': 'Grupo', 'db_table': "'grupo'"},
            'congregacao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Congregacao']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.publicador': {
            'Meta': {'object_name': 'Publicador', 'db_table': "'publicador'"},
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
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['main']