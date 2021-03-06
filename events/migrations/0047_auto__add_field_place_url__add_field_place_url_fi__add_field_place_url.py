# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Place.url'
        db.add_column('events_place', 'url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Place.url_fi'
        db.add_column('events_place', 'url_fi',
                      self.gf('django.db.models.fields.URLField')(null=True, max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Place.url_sv'
        db.add_column('events_place', 'url_sv',
                      self.gf('django.db.models.fields.URLField')(null=True, max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Place.url_en'
        db.add_column('events_place', 'url_en',
                      self.gf('django.db.models.fields.URLField')(null=True, max_length=200, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Place.url'
        db.delete_column('events_place', 'url')

        # Deleting field 'Place.url_fi'
        db.delete_column('events_place', 'url_fi')

        # Deleting field 'Place.url_sv'
        db.delete_column('events_place', 'url_sv')

        # Deleting field 'Place.url_en'
        db.delete_column('events_place', 'url_en')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'events.category': {
            'Meta': {'object_name': 'Category'},
            'aggregate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'alt_labels': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'categories'", 'to': "orm['events.CategoryLabel']", 'symmetrical': 'False', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events_category_created_by'", 'null': 'True', 'to': "orm['auth.User']", 'blank': 'True'}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'custom_fields': ('django_hstore.fields.DictionaryField', [], {'null': 'True', 'blank': 'True'}),
            'data_source': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['events.DataSource']", 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fi': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_sv': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'last_modified_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events_category_modified_by'", 'null': 'True', 'to': "orm['auth.User']", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'db_index': 'True'}),
            'name_fi': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'db_index': 'True'}),
            'name_sv': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'db_index': 'True'}),
            'origin_id': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'to': "orm['events.Category']", 'blank': 'True'}),
            'same_as': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'unknown'", 'db_index': 'True'})
        },
        'events.categorylabel': {
            'Meta': {'unique_together': "(('name', 'language'),)", 'object_name': 'CategoryLabel'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events_categorylabel_created_by'", 'null': 'True', 'to': "orm['auth.User']", 'blank': 'True'}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'data_source': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['events.DataSource']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Language']"}),
            'last_modified_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events_categorylabel_modified_by'", 'null': 'True', 'to': "orm['auth.User']", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'origin_id': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'db_index': 'True'})
        },
        'events.datasource': {
            'Meta': {'object_name': 'DataSource'},
            'event_url_template': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events_event_created_by'", 'null': 'True', 'to': "orm['auth.User']", 'blank': 'True'}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'custom_fields': ('django_hstore.fields.DictionaryField', [], {'null': 'True', 'blank': 'True'}),
            'data_source': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['events.DataSource']", 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fi': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_sv': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True', 'db_index': 'True'}),
            'event_status': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'to': "orm['events.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'last_modified_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['events.Place']", 'blank': 'True'}),
            'location_extra_info': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '400', 'blank': 'True'}),
            'location_extra_info_en': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '400', 'blank': 'True'}),
            'location_extra_info_fi': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '400', 'blank': 'True'}),
            'location_extra_info_sv': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '400', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events_event_modified_by'", 'null': 'True', 'to': "orm['auth.User']", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'db_index': 'True'}),
            'name_fi': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'db_index': 'True'}),
            'name_sv': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'db_index': 'True'}),
            'origin_id': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'db_index': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True', 'db_index': 'True'}),
            'super_event': ('mptt.fields.TreeForeignKey', [], {'related_name': "'sub_event'", 'null': 'True', 'to': "orm['events.Event']", 'blank': 'True'}),
            'target_group': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'url_en': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'url_fi': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'url_sv': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'})
        },
        'events.language': {
            'Meta': {'object_name': 'Language'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events_language_created_by'", 'null': 'True', 'to': "orm['auth.User']", 'blank': 'True'}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'data_source': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['events.DataSource']", 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'last_modified_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events_language_modified_by'", 'null': 'True', 'to': "orm['auth.User']", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'db_index': 'True'}),
            'name_fi': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'db_index': 'True'}),
            'name_sv': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'db_index': 'True'}),
            'origin_id': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'db_index': 'True'})
        },
        'events.openinghoursspecification': {
            'Meta': {'object_name': 'OpeningHoursSpecification'},
            'closes': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'days_of_week': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'opens': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'opening_hour_specification'", 'primary_key': 'True', 'unique': 'True', 'to': "orm['events.Place']"}),
            'valid_from': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'valid_through': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'events.place': {
            'Meta': {'unique_together': "(('data_source', 'origin_id'),)", 'object_name': 'Place'},
            'address_country': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '2', 'blank': 'True'}),
            'address_locality': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'address_locality_en': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'address_locality_fi': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'address_locality_sv': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'address_region': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'contact_type': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events_place_created_by'", 'null': 'True', 'to': "orm['auth.User']", 'blank': 'True'}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'custom_fields': ('django_hstore.fields.DictionaryField', [], {'null': 'True', 'blank': 'True'}),
            'data_source': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['events.DataSource']", 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fi': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_sv': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'last_modified_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'srid': '3067', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events_place_modified_by'", 'null': 'True', 'to': "orm['auth.User']", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'db_index': 'True'}),
            'name_fi': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'db_index': 'True'}),
            'name_sv': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'db_index': 'True'}),
            'origin_id': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'related_name': "'children'", 'null': 'True', 'to': "orm['events.Place']", 'blank': 'True'}),
            'post_office_box_num': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '128', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '128', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'same_as': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'db_index': 'True'}),
            'street_address': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'street_address_en': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'street_address_fi': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'street_address_sv': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '128', 'blank': 'True'}),
            'telephone_en': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '128', 'blank': 'True'}),
            'telephone_fi': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '128', 'blank': 'True'}),
            'telephone_sv': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '128', 'blank': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'url_en': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'url_fi': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'url_sv': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['events']