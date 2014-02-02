# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Gallery.seo_title_ru'
        db.add_column(u'gallery_gallery', 'seo_title_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Gallery.seo_title_en'
        db.add_column(u'gallery_gallery', 'seo_title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Gallery.seo_title_uk'
        db.add_column(u'gallery_gallery', 'seo_title_uk',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Gallery.seo_meta_ru'
        db.add_column(u'gallery_gallery', 'seo_meta_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Gallery.seo_meta_en'
        db.add_column(u'gallery_gallery', 'seo_meta_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Gallery.seo_meta_uk'
        db.add_column(u'gallery_gallery', 'seo_meta_uk',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Gallery.seo_title_ru'
        db.delete_column(u'gallery_gallery', 'seo_title_ru')

        # Deleting field 'Gallery.seo_title_en'
        db.delete_column(u'gallery_gallery', 'seo_title_en')

        # Deleting field 'Gallery.seo_title_uk'
        db.delete_column(u'gallery_gallery', 'seo_title_uk')

        # Deleting field 'Gallery.seo_meta_ru'
        db.delete_column(u'gallery_gallery', 'seo_meta_ru')

        # Deleting field 'Gallery.seo_meta_en'
        db.delete_column(u'gallery_gallery', 'seo_meta_en')

        # Deleting field 'Gallery.seo_meta_uk'
        db.delete_column(u'gallery_gallery', 'seo_meta_uk')


    models = {
        u'gallery.gallery': {
            'Meta': {'ordering': "('date', 'name')", 'object_name': 'Gallery'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'description': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'description_ru': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'description_uk': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'directory': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'seo_meta': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_meta_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_meta_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_meta_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'seo_title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'seo_title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'seo_title_uk': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'gallery.galleryimage': {
            'Meta': {'object_name': 'GalleryImage'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['gallery.Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['gallery']