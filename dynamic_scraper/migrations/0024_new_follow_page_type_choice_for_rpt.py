# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-06-14 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_scraper', '0023_added_follow_pages_by_xpath_and_num_pages_follow_atts_to_scraper_pagination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestpagetype',
            name='page_type',
            field=models.CharField(choices=[('MP', 'Main Page'), ('FP', 'Follow Page'), ('DP1', 'Detail Page 1'), ('DP2', 'Detail Page 2'), ('DP3', 'Detail Page 3'), ('DP4', 'Detail Page 4'), ('DP5', 'Detail Page 5'), ('DP6', 'Detail Page 6'), ('DP7', 'Detail Page 7'), ('DP8', 'Detail Page 8'), ('DP9', 'Detail Page 9'), ('DP10', 'Detail Page 10'), ('DP11', 'Detail Page 11'), ('DP12', 'Detail Page 12'), ('DP13', 'Detail Page 13'), ('DP14', 'Detail Page 14'), ('DP15', 'Detail Page 15'), ('DP16', 'Detail Page 16'), ('DP17', 'Detail Page 17'), ('DP18', 'Detail Page 18'), ('DP19', 'Detail Page 19'), ('DP20', 'Detail Page 20'), ('DP21', 'Detail Page 21'), ('DP22', 'Detail Page 22'), ('DP23', 'Detail Page 23'), ('DP24', 'Detail Page 24'), ('DP25', 'Detail Page 25')], help_text='One main page RPT, an optional follow page RPT (if follow pagination is used) and detail page RPTs for all DETAIL_PAGE_URLs', max_length=3),
        ),
    ]