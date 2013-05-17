# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Grupo'
        db.create_table('grupo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['Grupo'])

        # Adding model 'Publicador'
        db.create_table('publicador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Grupo'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('endereco', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('nascimento', self.gf('django.db.models.fields.DateField')()),
            ('batismo', self.gf('django.db.models.fields.DateField')()),
            ('anciao', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('servo_ministerial', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pioneiro_regular', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'main', ['Publicador'])


    def backwards(self, orm):
        # Deleting model 'Grupo'
        db.delete_table('grupo')

        # Deleting model 'Publicador'
        db.delete_table('publicador')


    models = {
        u'main.grupo': {
            'Meta': {'object_name': 'Grupo', 'db_table': "'grupo'"},
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