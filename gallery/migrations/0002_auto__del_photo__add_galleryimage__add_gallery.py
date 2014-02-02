# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Photo'
        db.delete_table(u'gallery_photo')

        # Adding model 'GalleryImage'
        db.create_table(u'gallery_galleryimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['gallery.Gallery'])),
            ('image', self.gf('filebrowser.fields.FileBrowseField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'gallery', ['GalleryImage'])

        # Adding model 'Gallery'
        db.create_table(u'gallery_gallery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name_ru', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name_uk', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('description', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('description_ru', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('description_en', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('description_uk', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'gallery', ['Gallery'])


    def backwards(self, orm):
        # Adding model 'Photo'
        db.create_table(u'gallery_photo', (
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description_uk', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_ru', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('img', self.gf('filebrowser.fields.FileBrowseField')(max_length=255)),
            ('name_uk', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description_ru', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'gallery', ['Photo'])

        # Deleting model 'GalleryImage'
        db.delete_table(u'gallery_galleryimage')

        # Deleting model 'Gallery'
        db.delete_table(u'gallery_gallery')


    models = {
        u'gallery.gallery': {
            'Meta': {'ordering': "('date', 'name')", 'object_name': 'Gallery'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'description': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'description_ru': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'description_uk': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'gallery.galleryimage': {
            'Meta': {'object_name': 'GalleryImage'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['gallery.Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['gallery']