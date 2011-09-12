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

from django.conf.urls.defaults import patterns, url
from project.views import view_projects, configure_project, add_project, view_results, view_single_result, launch_project, add_schedule, project_wizard
from project.forms import ProjectFormWizard, ProjectForm1, ProjectForm2, ProjectForm3, ProjectForm4

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('project.views',
                       
    url(r'^$', view_projects, name='view_project'),
    url(r'^wizard/$', project_wizard, name='project_wizard'),
    url(r'^create/$', ProjectFormWizard([ProjectForm1, ProjectForm2, ProjectForm3, ProjectForm4]), name='create'),
    url(r'^add/$', add_project, name='add_project'),
    url(r'^add/schedule/$', add_schedule, name='add_schedule'),
    url(r'^configure/(\d+)$', configure_project, name='configure_project'),
    url(r'^launch/(\d+)$', launch_project, name='launch_project'),   
    url(r'^result/(\d+)$', view_results, name='view_results'),
    url(r'^result/(\d+)/(\d+)$', view_single_result, name='view_single_result'),
)
