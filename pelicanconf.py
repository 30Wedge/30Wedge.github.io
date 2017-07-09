# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#Content
AUTHOR = 'Andy MacGregor'
SITENAME = 'Andy MacGregor'
SITEURL = '' #unspecified causes no problems
PYGMENTS_STYLE = 'monokai'

#Config
THEME = 'Flex'
PATH = 'content'
PATH_PAGES = ['pages']
DEFAULT_DATE = 'fs'
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True
CACHE_CONTENT = False

#Local
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

#Nothing I need here
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget - nty
#SOCIAL = (('You can add links in your config file', '#'),

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
