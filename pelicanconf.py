#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"David Johansen"
SITENAME = u"rhce.co"
SITEURL = ''

GITHUB_URL = 'https://github.com/makewhatis/rhce.co'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

#THEME = 'pelican-bootstrap-responsive-theme'
THEME = 'rhce-theme'
# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

SUMMARY_MAX_LENGTH = 40

EXAMS = ['RHCSA', 'RHCE']


ARTICLE_URL = ('{slug}.html')
