# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 23:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracktopics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertotrack',
            old_name='word_text',
            new_name='user_text',
        ),
    ]