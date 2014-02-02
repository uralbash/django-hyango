# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Banner'
        db.create_table(u'pages_banner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('filebrowser.fields.FileBrowseField')(max_length=255, null=True, blank=True)),
            ('text', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'pages', ['Banner'])

        # Adding field 'Page.in_main'
        db.add_column(u'pages_page', 'in_main',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Page.in_footer'
        db.add_column(u'pages_page', 'in_footer',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Page.content'
        db.alter_column(u'pages_page', 'content', self.gf('tinymce.models.HTMLField')(null=True))

    def backwards(self, orm):
        # Deleting model 'Banner'
        db.delete_table(u'pages_banner')

        # Deleting field 'Page.in_main'
        db.delete_column(u'pages_page', 'in_main')

        # Deleting field 'Page.in_footer'
        db.delete_column(u'pages_page', 'in_footer')


        # Changing field 'Page.content'
        db.alter_column(u'pages_page', 'content', self.gf('django.db.models.fields.TextField')(null=True))

    models = {
        u'pages.banner': {
            'Meta': {'ordering': "('sort', 'name')", 'object_name': 'Banner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'text': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'pages.page': {
            'Meta': {'ordering': "('path', 'url', 'name')", 'object_name': 'Page'},
            'content': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_footer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'in_header': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'in_main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lock': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'redirect_to': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'seo_meta': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['pages']