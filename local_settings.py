# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2012 OpenPlans
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
#
#########################################################################

# Django settings for the GeoNode project.
import os
from kombu import Queue
from celery_app import app  # flake8: noqa

#
# General Django development settings
#

# Defines the directory that contains the settings file as the PROJECT_ROOT
# It is used for relative settings elsewhere.
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Setting debug to true makes Django serve static media and
# present pretty error pages.
DEBUG = TEMPLATE_DEBUG = True

# Set to True to load non-minified versions of (static) client dependencies
# Requires to set-up Node and tools that are required for static development
# otherwise it will raise errors for the missing non-minified dependencies
DEBUG_STATIC = False

# This is needed for integration tests, they require
# geonode to be listening for GeoServer auth requests.
os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = 'localhost:8000'

# Defines settings for development

POSTGIS_VERSION = (2,1,2)
SITEURL = "http://localhost:8000/"

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', # Empty ENGINE name disables 
        'NAME': 'geonode',
        'USER' : 'geonode',
        'PASSWORD' : 'geonode',
        'HOST' : '127.0.0.1',
        'PORT' : '5432',
     },
}

##DATABASES = {
##    'default': {
##         'ENGINE': 'django.db.backends.postgresql_psycopg2',
##         'NAME': 'geonode',
##         'USER': 'geonode',
##         'PASSWORD': 'geonode',
##     },

##    # vector datastore for uploads
##    'datastore' : {
##        #'ENGINE': 'django.contrib.gis.db.backends.postgis',
##        'ENGINE': '', # Empty ENGINE name disables 
##        'NAME': 'geonode',
##        'USER' : 'geonode',
##        'PASSWORD' : 'geonode',
##        'HOST' : 'localhost',
##        'PORT' : '5432',
##    }
##}

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default' : {
        'BACKEND' : 'geonode.geoserver',
        'LOCATION' : 'http://localhost:8080/geoserver/',
        'PUBLIC_LOCATION' : 'http://localhost:8080/geoserver/',
        'USER' : 'admin',
        'PASSWORD' : 'geoserver',
        'MAPFISH_PRINT_ENABLED' : True,
        'PRINT_NG_ENABLED' : True,
        'GEONODE_SECURITY_ENABLED' : True,
        'GEOGIG_ENABLED' : False,
        'WMST_ENABLED' : False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED' : False,
        'LOG_FILE': '%s/geoserver/data/logs/geoserver.log' % os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir)),
        # Set to name of database in DATABASES dictionary to enable
        'DATASTORE': '', #'datastore',
    }
}

CATALOGUE = {
    'default': {
        # The underlying CSW implementation
        # default is pycsw in local mode (tied directly to GeoNode Django DB)
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        # pycsw in non-local mode
        # 'ENGINE': 'geonode.catalogue.backends.pycsw_http',
        # GeoNetwork opensource
        # 'ENGINE': 'geonode.catalogue.backends.geonetwork',
        # deegree and others
        # 'ENGINE': 'geonode.catalogue.backends.generic',

        # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
        'URL': '%scatalogue/csw' % SITEURL,
        # 'URL': 'http://localhost:8080/geonetwork/srv/en/csw',
        # 'URL': 'http://localhost:8080/deegree-csw-demo-3.0.4/services',

        # login credentials (for GeoNetwork)
        'USER': 'admin',
        'PASSWORD': 'admin',
    }
}

# Default preview library
#LAYER_PREVIEW_LIBRARY = 'geoext'
