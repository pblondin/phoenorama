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

'''
Created on Mar 3, 2011

@author: r00tmac
'''
from django.forms import ModelForm, Form
from django import forms
from django.contrib.formtools.wizard import FormWizard
from project.models import Project, Schedule
from django.forms.models import ModelChoiceField
from management.forms import SelectWithPop
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response


class ProjectForm(ModelForm):
    schedule = ModelChoiceField(Schedule.objects, widget=SelectWithPop)
    class Meta:
        model = Project
        exclude = ('creator',)
        
class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        
class ProjectForm1(Form):
    agreement = forms.BooleanField(required=True)

class ProjectForm2(Form):
    name = forms.CharField()
    agreement = forms.CheckboxInput()

class ProjectForm3(Form):
    name = forms.CharField()
    agreement = forms.CheckboxInput()

class ProjectForm4(Form):
    name = forms.CharField()
    agreement = forms.CheckboxInput()

class ProjectFormWizard(FormWizard):
    name = forms.CharField()
    agreement = forms.CheckboxInput()
    
    def done(self, request, form_list):
        return render_to_response('done.html', {
            'form': [form.cleaned_data for form in form_list],
        })
    
    def get_template(self, step):
        return ['project/project_wizard_%s.html' % step, 'project/project_wizard.html']
    
    
    
    

