# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 05:27
from __future__ import unicode_literals

from django.db import migrations

from django.contrib.postgres.operations import TrigramExtension

class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        TrigramExtension()
    ]