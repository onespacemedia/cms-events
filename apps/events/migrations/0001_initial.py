# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.apps.media.models
import django.db.models.deletion
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_file_alt_text'),
        ('pages', '0006_auto_20151002_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_online', models.BooleanField(default=True, help_text="Uncheck this box to remove the page from the public website. Logged-in admin users will still be able to view this page by clicking the 'view on site' button.", verbose_name='online')),
                ('browser_title', models.CharField(help_text="The heading to use in the user's web browser. Leave blank to use the page title. Search engines pay particular attention to this attribute.", max_length=1000, blank=True)),
                ('meta_description', models.TextField(help_text='A brief description of the contents of this page.', verbose_name='description', blank=True)),
                ('sitemap_priority', models.FloatField(default=None, choices=[(1.0, 'Very high'), (0.8, 'High'), (0.5, 'Medium'), (0.3, 'Low'), (0.0, 'Very low')], blank=True, help_text='The relative importance of this content on your site. Search engines use this as a hint when ranking the pages within your site.', null=True, verbose_name='priority')),
                ('sitemap_changefreq', models.IntegerField(default=None, choices=[(1, 'Always'), (2, 'Hourly'), (3, 'Daily'), (4, 'Weekly'), (5, 'Monthly'), (6, 'Yearly'), (7, 'Never')], blank=True, help_text='How frequently you expect this content to be updated. Search engines use this as a hint when scanning your site for updates.', null=True, verbose_name='change frequency')),
                ('robots_index', models.BooleanField(default=True, help_text='Uncheck to prevent search engines from indexing this page. Do this only if the page contains information which you do not wish to show up in search results.', verbose_name='allow indexing')),
                ('robots_follow', models.BooleanField(default=True, help_text='Uncheck to prevent search engines from following any links they find in this page. Do this only if the page contains links to other sites that you do not wish to publicise.', verbose_name='follow links')),
                ('robots_archive', models.BooleanField(default=True, help_text='Uncheck this to prevent search engines from archiving this page. Do this this only if the page is likely to change on a very regular basis. ', verbose_name='allow archiving')),
                ('og_title', models.CharField(help_text='Title that will appear on Facebook posts. This is limited to 100 characters, but Facebook will truncate the title to 88 characters.', max_length=100, verbose_name='title', blank=True)),
                ('og_description', models.TextField(help_text='Description that will appear on Facebook posts. It is limited to 300 characters, but it is recommended that you do not use anything over 200.', max_length=300, verbose_name='description', blank=True)),
                ('twitter_card', models.IntegerField(default=None, choices=[(0, 'Summary'), (1, 'Photo'), (2, 'Video'), (3, 'Product'), (4, 'App'), (5, 'Gallery'), (6, 'Large Summary')], blank=True, help_text='The type of content on the page. Most of the time "Summary" will suffice. Before you can benefit from any of these fields make sure to go to https://dev.twitter.com/docs/cards/validation/validator and get approved.', null=True, verbose_name='card')),
                ('twitter_title', models.CharField(help_text='The title that appears on the Twitter card, it is limited to 70 characters.', max_length=70, verbose_name='title', blank=True)),
                ('twitter_description', models.TextField(help_text="Description that will appear on Twitter cards. It is limited to 200 characters. This does'nt effect SEO, so focus on copy that complements the tweet and title rather than on keywords.", max_length=200, verbose_name='description', blank=True)),
                ('slug', models.SlugField(help_text='A user friendly URL')),
                ('title', models.CharField(max_length=1000)),
                ('short_title', models.CharField(help_text='A shorter version of the title that will be used in site navigation. Leave blank to use the full-length title.', max_length=200, blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('key_info', models.TextField(help_text=b'This is the content that appears below the title in the hero', null=True, blank=True)),
                ('description', cms.models.fields.HtmlField()),
                ('image', cms.apps.media.models.ImageRefField(related_name='+', on_delete=django.db.models.deletion.PROTECT, blank=True, to='media.File', null=True)),
                ('og_image', cms.apps.media.models.ImageRefField(related_name='+', on_delete=django.db.models.deletion.PROTECT, blank=True, to='media.File', help_text='The recommended image size is 1200x627 (1.91:1 ratio); this gives you a big stand out thumbnail. Using an image smaller than 400x209 will give you a small thumbnail and will splits posts into 2 columns. If you have text on the image make sure it is centered.', null=True, verbose_name='image')),
            ],
            options={
                'ordering': ('start_date',),
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('page', models.OneToOneField(related_name='+', primary_key=True, serialize=False, editable=False, to='pages.Page')),
                ('hero_super_title', models.CharField(help_text=b'This is the small text that is above the title, if this is left empty it will take the pages title', max_length=50, null=True, blank=True)),
                ('hero_title', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='event',
            name='page',
            field=models.ForeignKey(to='events.Events'),
        ),
        migrations.AddField(
            model_name='event',
            name='twitter_image',
            field=cms.apps.media.models.ImageRefField(related_name='+', on_delete=django.db.models.deletion.PROTECT, blank=True, to='media.File', help_text='The minimum size it needs to be is 280x150. If you want to use a larger imagemake sure the card type is set to "Large Summary".', null=True, verbose_name='image'),
        ),
    ]
