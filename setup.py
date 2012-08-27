#!/usr/bin/env python
#
# RedGear - an application service monitoring system.
#
# Copyright (C) 2012 TinySoft, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
RedGear installer
"""

import os, sys
from distutils.core import setup

import redgear

scripts = ["bin/rgmaster",
           "bin/rgslave"]

setup_args = {
    'name': "redgear",
    'version': redgear.__version__,
    'description': "RedGear monitoring system",
    'long_description': redgear.__doc__,
    'author': redgear.__author__,
    'author_email': "mail@mail.com",
    'url': "https://github.com/tomnotcat/redgear",
    'license': redgear.__license__,
    'platforms': "any",
    'classifiers': [
        'Development Status :: 1 - Planning',
        'Environment :: No Input/Output (Daemon)',
        'Framework :: Twisted',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Topic :: System :: Monitoring',
        ],
    'packages': [
        "redgear",
        "redgear.test",
        ],
    'scripts': scripts,
    }

# set zip_safe to false to force Windows installs to always unpack eggs
# into directories, which seems to work better --
# see http://buildbot.net/trac/ticket/907
if sys.platform == "win32":
    setup_args['zip_safe'] = False

try:
    # If setuptools is installed, then we'll add setuptools-specific arguments
    # to the setup args.
    import setuptools #@UnusedImport
except ImportError:
    pass
else:
    setup_args['install_requires'] = ['twisted >= 8.0.0',]

    if os.getenv('NO_INSTALL_REQS'):
        setup_args['install_requires'] = None

setup(**setup_args)
