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
Created on Feb 28, 2011

@author: r00tmac
'''
from project.models import *
from django.contrib import admin

class OwnerAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

class TargetAdmin(admin.ModelAdmin):
    pass

class ScheduleAdmin(admin.ModelAdmin):
    pass

class ProfileAdmin(admin.ModelAdmin):
    pass

class TaskAdmin(admin.ModelAdmin):
    pass

class TaskTemplateAdmin(admin.ModelAdmin):
    pass

class ToolAdmin(admin.ModelAdmin):
    pass

class ConfigAdmin(admin.ModelAdmin):
    pass

class ResultAdmin(admin.ModelAdmin):
    pass

class OpenVASTaskAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskTemplate, TaskTemplateAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(Config, ConfigAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(OpenVASTask, OpenVASTaskAdmin)

