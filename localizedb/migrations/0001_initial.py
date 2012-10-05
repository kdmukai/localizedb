# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FieldGroup'
        db.create_table('localizedb_fieldgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('localizedb', ['FieldGroup'])

        # Adding model 'TranslatedField'
        db.create_table('localizedb_translatedfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['localizedb.FieldGroup'])),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('translation', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal('localizedb', ['TranslatedField'])


    def backwards(self, orm):
        # Deleting model 'FieldGroup'
        db.delete_table('localizedb_fieldgroup')

        # Deleting model 'TranslatedField'
        db.delete_table('localizedb_translatedfield')


    models = {
        'localizedb.fieldgroup': {
            'Meta': {'object_name': 'FieldGroup'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'localizedb.translatedfield': {
            'Meta': {'object_name': 'TranslatedField'},
            'field_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localizedb.FieldGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'translation': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['localizedb']