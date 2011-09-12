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

from datetime import date
import time
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, Http404
from django.template.context import RequestContext

from management.views import handlePopAdd
from project.tools.openvas import Openvas
from project.forms import ProjectForm, ScheduleForm
from project.models import Project, OpenVASTask


def project_wizard(request):
    return render_to_response('project/project_wizard.html', RequestContext(request, locals()))

def view_projects(request):
    '''
    View projects of the current user.
    '''
    projects = get_list_or_404(Project, creator=request.user)
    return render_to_response('project/view_projects.html', RequestContext(request, locals()))

def add_project(request):
    '''
    Create a new project for the current user.
    '''
    if request.method == 'POST': 
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.creator = request.user
            project.save()
            return render_to_response('account/my_account.html', RequestContext(request, locals()))
    else:
        form = ProjectForm()
    return render_to_response('project/add_project.html', RequestContext(request, locals()))

def add_schedule(request):
    '''
    Create a new schedule for the current user.
    '''
    if '_popup' in request.GET and request.GET['_popup'] == '1':
        return handlePopAdd(request, ScheduleForm, 'schedule') 
    if request.method == 'POST': 
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('account/my_account.html', RequestContext(request, locals()))
    else:
        form = ScheduleForm()
    return render_to_response('project/add_schedule.html', RequestContext(request, locals()))

def view_results(request, project_id):
    '''
    View the results of a project.
    '''
    if request.method == 'GET':
        my_project = get_object_or_404(Project, pk=project_id)
        result_list = get_list_or_404(OpenVASTask, project=my_project)
        return render_to_response('project/view_results.html', RequestContext(request, locals()))
    return render_to_response('account/my_account.html', RequestContext(request, locals()))

def view_single_result(request, project_id, result_id):
    '''
    View a single result.
    '''
    if request.method == 'GET':
        my_project = get_object_or_404(Project, pk=project_id)
        my_task = get_object_or_404(OpenVASTask, pk=result_id)
        if my_task.state == 'e': # Task has finished
            finish = True
            try:
                results = my_task.results.all()
            except IOError:
                raise Http404
        else:
            finish = False
        return render_to_response('project/view_single_result.html', RequestContext(request, locals()))
    return render_to_response('account/my_account.html', RequestContext(request, locals()))
        
def configure_project(request):
    '''
    Configure the project of a user.
    '''
    pass

def launch_project(request, project_id):
    '''
    Launch a project. (i.e start the scan)
    '''  
    if request.method == 'GET':    
        my_project = get_object_or_404(Project, pk=project_id)        
        task = OpenVASTask(project=my_project, state='c', 
                               nbeFile='project_id_%s_%s_%s.nbe' % (str(my_project.id), date.today(), time.time()),
                               targetFile='target_project_id_%s.txt' %(str(my_project.id)))
        task.save()

        o = Openvas(task.id)
        o.configure(targetFile=task.targetFile, nbeFile=task.nbeFile)
        o.start()
            
    return render_to_response('project/launch_project.html', RequestContext(request, locals()))










