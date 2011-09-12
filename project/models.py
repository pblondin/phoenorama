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

from django.db import models
from django.contrib.auth.models import User
from infosec.models import CVE, BUGTRAQ, NVT

##############################
## PROJECT
##############################
class ProjectManager(models.Manager):
    def fromCreator(self, creator):
        self.get_query_set().filter(creator=creator)

class Project(models.Model):
    creator = models.ForeignKey(User, unique=False)   
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)    
    create_time = models.DateTimeField(auto_now_add=True)
    target = models.IPAddressField()
    schedule = models.ForeignKey('Schedule')
    
    # Subscribe the ProjectManager    
    objects = ProjectManager()
       
    class Meta:
        db_table = u'project'
        
    def __unicode__(self):
        return u'%s , %s' % (self.name, self.description)
    
##############################
## SCHEDULE 
##############################
class Schedule(models.Model):
    FREQUENCY_CHOICES = (
        (u'd', u'Daily'),
        (u'w', u'Weekly'),
        (u'm', u'Monthly'),
    )
    
    name = models.CharField(max_length=50)
    comment = models.TextField(null=True, blank=True)
    first_time = models.DateTimeField()
    frequency = models.CharField(max_length=1, choices=FREQUENCY_CHOICES)
    last_time = models.DateTimeField()
    
    class Meta:
        db_table = u'schedule'
        
    def __unicode__(self):
        return str(self.name)

##############################
## PROFILE 
##############################    
class Profile(models.Model):
    name = models.CharField(max_length=50)
    task_templates = models.ManyToManyField('TaskTemplate')
    comment = models.TextField()
    
    class Meta:
        db_table = u'profile'
        
    def __unicode__(self):
        return u"Profile: id [%s], Name [%s], Comment [%s]" % (str(self.id), self.name, self.comment)

##############################
## TASK_TEMPLATE MODEL 
##############################
class TaskTemplate(models.Model):
    name = models.CharField(max_length=50)
    tool = models.ForeignKey('Tool')
    config = models.ForeignKey('Config')
    
    class Meta:
        db_table = u'task_template'
        
    def __unicode__(self):
        return u"Task: id [%s], Name [%s], Tool_id [%s], Config_id [%s]" % (str(self.id), self.name, str(self.tool.id), str(self.config.id))

##############################
## TASK 
##############################
class Task(models.Model):
    STATE_CHOICES = (
        (u'c', u'Created'),
        (u'a', u'Attribute'),
        (u's', u'Started'),
        (u'p', u'Paused'),
        (u'e', u'Ended'),
    )
    
    #target = models.ForeignKey('Target')
    result = models.ForeignKey('Result')
    create_time = models.DateTimeField(auto_now_add=True)
    scan_time = models.DateTimeField()
    state = models.CharField(max_length=1, choices=STATE_CHOICES)
    version_ruleset = models.CharField(max_length=20)
    version_tool = models.CharField(max_length=20)
    
    class Meta:
        db_table = u'task'
        
    def __unicode__(self):
        return u"Execution_task: id [%s], Target_id [%s], Task_id [%s]" % (str(self.id), str(self.target.id), str(self.task.id))
    
##############################
## TOOL 
##############################  
class Tool(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = u'tool'
        
    def __unicode__(self):
        return u"Tool: id [%s]" % (str(self.id))

##############################
## CONFIG
##############################  
class Config(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = u'config'
        
    def __unicode__(self):
        return u"Config: id [%s]" % (str(self.id))
    

##############################
## OPENVAS_TASK
##############################
class OpenVASTask(models.Model):
    STATE_CHOICES = (
        (u'c', u'Created'),
        (u'a', u'Attribute'),
        (u's', u'Started'),
        (u'p', u'Paused'),
        (u'e', u'Ended'),
        (u'x', u'Error'),
    )
    project = models.ForeignKey('Project')
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='c')
    nbeFile = models.FilePathField(path="./resources/results/", match="^project_*", default="")
    targetFile = models.FilePathField(path="./resources/results/", match="^target_*", default="")
    results = models.ManyToManyField('Result', null=True, blank=True, symmetrical=False)
    
    def __unicode__(self):
        return u"Task for project [%s]" % (str(self.project.id))    

##############################
## RESULT
##############################  
class Result(models.Model):
    RISK_FACTOR = (
        (u'c', u'Critical'),
        (u'h', u'High'),
        (u'm', u'Medium'),
        (u'l', u'Low'),
        (u'i', u'Informative'),
        (u'u', u'Unknown'),
        (u'f', u'False positive'),
    )
    
    title = models.CharField(max_length=150, default='')
    summary = models.CharField(max_length=200, default='')
    target = models.CharField(max_length=50, default='')
    description = models.TextField(null=True, blank=True)
    service = models.CharField(max_length=50, null=True, blank=True)
    nvt = models.ForeignKey(NVT, null=True, blank=True)
    cve = models.ForeignKey(CVE, null=True, blank=True)
    bid = models.ForeignKey(BUGTRAQ, null=True, blank=True)
    risk_factor = models.CharField(max_length=1, choices=RISK_FACTOR, default='u')
    
    class Meta:
        db_table = u'result'
        
    def __unicode__(self):
        return u"Result: id [%s]" % (str(self.id))

