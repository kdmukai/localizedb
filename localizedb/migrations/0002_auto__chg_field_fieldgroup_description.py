# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'FieldGroup.description'
        db.alter_column('localizedb_fieldgroup', 'description', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

    def backwards(self, orm):

        # Changing field 'FieldGroup.description'
        db.alter_column('localizedb_fieldgroup', 'description', self.gf('django.db.models.fields.CharField')(default=None, max_length=128))

    models = {
        'localizedb.fieldgroup': {
            'Meta': {'object_name': 'FieldGroup'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
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