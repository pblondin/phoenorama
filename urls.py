#######
#
# Copyright (C) 2011 Phoenorama.org All Rights Reserved.
# Author: Philippe Blondin <pblondin@phoenorama.org>>
#
# This file is part of the Phoenorama program.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING.  If not, write to
# the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#
#######

from django.conf.urls.defaults import patterns, include
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^Phoenorama_FE/', include('Phoenorama_FE.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    # URL pattern for Django-Sentry
    (r'^sentry/', include('sentry.urls')),

    # Include URL pattern for the Management apps
    (r'^', include('management.urls')),
    
    # Include URL pattern for the Account apps
    #(r'^', include('account.urls')),
    
    # Registration
    (r'^account/', include('account.urls')),
    (r'^account/', include('registration.urls')),

    
    # Include URL pattern for the Project apps
    (r'^project/', include('project.urls')),
    

)


if settings.DEBUG:
    urlpatterns += patterns('',
        # Include Static Media Files
        (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + "/css/"}),
        (r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + "/img/"}),
        (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + "/js/"}),
    )
