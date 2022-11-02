#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Michael Jeronimo'
SITENAME = 'SpaceROS'
SITEDESCRIPTION = 'The Space ROS website'
#SITEURL = 'https://space-ros.github.io/spaceros.org'
SITEURL = 'http://localhost:8081'

# Plugins
PLUGIN_PATHS = ['../plugins/']
PLUGINS = [ 
  'i18n_subsites', 
  'pelican_youtube', 
  'pelican_vimeo',
]

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Theme and theme localization
THEME = '../theme'
I18N_GETTEXT_LOCALEDIR = '../theme/locale/'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True
TIMEZONE = 'Europe/Zurich'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
I18N_TEMPLATES_LANG = 'en_US'
DEFAULT_LANG = 'en'
LOCALE = 'en_US'

# Content paths
PATH = 'content'
PAGE_PATHS = ['pages/en']
ARTICLE_PATHS = ['blog/en']

# I18n
I18N_SUBSITES = {
  'de': {
    'PAGE_PATHS': ['pages/de'],
    'ARTICLE_PATHS': ['blog/de'],
    'LOCALE': 'de_DE'
  }
}

# Logo path, needs to be stored in PATH Setting
LOGO = '/images/logo.svg'

# Special content
HERO = [
  {
    'image': '/images/hero/background-1.png',
    # for multilanguage support, create a simple dict
    'title': {
      'en':'Space ROS',
      'de': 'Space ROS'
    },
    'text': {
      'en': 'An open-source space robotics framework for developing flight-quality robotic and autonomous space systems',
      'de': 'Jeglicher spezieller Inhalt den Sie hier bewerben möchten'
    },
    'links': [
      {
        'icon': 'icon-code',  # icon-code
        'url': 'https://space-ros.github.io/docs/rolling/index.html',
        'text': 'Read the docs'
      }
    ]
  }, {
    # keep it a string if you dont need multiple languages
    'image': '/images/hero/background-2.jpg',
    'title': 'Our Goal',
    # keep it a string if you dont need multiple languages
    'text': 'Ease the adoption of the popular ROS framework into space robotics systems',
    'links': []
  }, {
    'image': '/images/hero/background-3.jpg',
    'title': 'Certification-Ready',
    'text': 'Space ROS will provide software and artifacts that are aligned with aerospace standards',
    'links': []
  }, {
    'image': '/images/hero/background-4.jpg',
    'title': 'Open Source and Open Community',
    'text': 'Bring the benefits of ROS to space robotics',
    'links': []
  }
]

# Social widget
SOCIAL = (
  ('Github', 'https://github.com/space-ros'),
  ('Twitter', 'https://twitter.com/search?q=%23spaceros&src=typed_query#spaceros'),
  ('LinkedIn', 'https://www.linkedin.com/search/results/all/?keywords=%23spaceros&origin=GLOBAL_SEARCH_HEADER&sid=fB8'),
)

ABOUT = {
  'image': '/images/about/about.svg',
  'mail': 'info@spaceros.org',
  # keep it a string if you dont need multiple languages
  'text': {
    'en': 'Drop us a message.',
    'de': 'Lernen Sie den Author kennen oder hinterlassen Sie einfach eine Nachricht'
  },
  'link': 'contact.html',
  # the address is also taken for google maps
  'address': 'Mt. View, CA',
  'phone': '+1 650-450-9681',
}

# Navigation and homepage options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
PAGE_ORDER_BY = 'order'

MENUITEMS = [
  ('Archive', 'archives.html'),
  ('Contact', 'contact.html')
]

DIRECT_TEMPLATES = [
  'index',
  'tags',
  'categories',
  'authors',
  'archives',
#  'search', # needed for tipue_search plugin
  'contact' # needed for the contact form
]

# Setup disqus
DISQUS_SHORTNAME = 'gitcd-dev'
DISQUS_ON_PAGES = False # if true its just displayed on every static page, like this you can still enable it per page

# Setup google maps
GOOGLE_MAPS_KEY = 'AIzaSyCefOgb1ZWqYtj7raVSmN4PL2WkTrc-KyA'
