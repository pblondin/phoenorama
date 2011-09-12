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


##############################
## CVE MODEL 
##############################
class CVE(models.Model):
    id = models.IntegerField(primary_key=True)


##############################
## BUGTRAQ MODEL 
##############################
class BUGTRAQ(models.Model):
    id = models.IntegerField(primary_key=True)


##############################
## NVT MODEL 
##############################
class NVT(models.Model):
    id = models.IntegerField(primary_key=True)
    oid = models.CharField(max_length=100, unique=True)
    version = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    description = models.TextField()
    copyright = models.CharField(max_length=100, null=True, blank=True)
    cve = models.CharField(max_length=255, null=True, blank=True)
    bid = models.CharField(max_length=255, null=True, blank=True)
    xref = models.CharField(max_length=255, null=True, blank=True)
    tag = models.CharField(max_length=255, null=True, blank=True)
    sign_key_ids = models.CharField(max_length=30, null=True, blank=True)
    category = models.IntegerField(null=True, blank=True)
    family = models.CharField(max_length=100, null=True, blank=True)
    cvss_base = models.FloatField(null=True, blank=True)
    risk_factor = models.CharField(max_length=10, null=True, blank=True)
    
    class Meta:
        db_table = u'nvts'
        ordering = ('oid',)
        
    def __unicode__(self):
        return self.name + " (" + self.oid + ")" 
    
##############################
## OVERRIDE MODEL 
##############################
THREAT_LEVELS = (
    ('C', 'Critical'),
    ('M', 'Medium'),
    ('L', 'Low'),
    ('F', 'False positive'),
)

class Override(models.Model):
    nvt = models.ForeignKey(NVT, unique=True)
    threat = models.CharField(max_length=1, choices=THREAT_LEVELS)
    description = models.TextField()
    last_edit = models.DateField()
    user_edit = models.CharField(max_length=30)
    
    class Meta:
        db_table = u'override'
    
    def __unicode__(self):
        return "Override: " + self.nvt.oid


