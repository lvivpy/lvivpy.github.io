#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGINS = [
    'pelican_youtube',
]

AUTHOR = 'LvivPy'
SITENAME = 'Lviv Python Community'
SITEURL = 'https://lvivpy.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ATOM = 'feeds.xml'
FEED_RSS = 'rss.xml'
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images']
DISPLAY_CATEGORIES_ON_MENU = False

THEME = 'themes/brutalist'
LOGO = 'logo.png'
FIRST_NAME = 'LvivPy'
TELEGRAM = 'https://t.me/lviv_python_community'
YOUTUBE = 'https://www.youtube.com/channel/UCrOhS-i7MaNMXCxJjjHYBQA'
#PLUGINS = ['w3c_validate', 'optimize_images', 'gzip_cache']
