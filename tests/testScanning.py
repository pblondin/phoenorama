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

# settings.py
import sys
import datetime
from django.conf import settings

settings.configure(
    DATABASE_ENGINE='django.db.backends.sqlite3',
    DATABASE_NAME='/home/django/Phoenorama_FE/src/sqlite.db', #os.path.join(os.path.dirname(__file__), 'sqlite.db').replace('\\','/'),
    DATABASE_USER='',
    DATABASE_PASSWORD='',
    DATABASE_HOST='',
    DATABASE_PORT='',
    INSTALLED_APPS=('scanning', 'south'),
)

# add project path
sys.path.append("/home/django/Phoenorama_FE/src")

from django.db import *
from scanning.models import *

def deleteObjects():
	objects = {}
	objects['owners'] = Owner.objects.all()
	objects['targets'] = Target.objects.all()
	objects['schedules'] = Schedule.objects.all()
	objects['profiles'] = Profile.objects.all()
	objects['projects'] = Project.objects.all()
	
	for o in objects:
		objects[o].delete()
		
def printObjects():
	objects = {}
	objects['owners'] = Owner.objects.all()
	objects['targets'] = Target.objects.all()
	objects['schedules'] = Schedule.objects.all()
	objects['profiles'] = Profile.objects.all()
	objects['projects'] = Project.objects.all()
	
	for o in objects:
		print "[ " + o + " ]" 
		for item in objects[o]:
			print item
		print ""
	
if __name__ == '__main__':

	# Delete all objects
	deleteObjects()

	# Create a owner
	o = Owner()
	o.name = "Philippe"
	o.email = "asdf@asdf.com"
	o.save()

	# Create two targets
	t1 = Target()
	t1.address = "127.0.0.1"
	t1.save()

	t2 = Target()
	t2.address = "192.168.0.0"
	t2.save()

	# Create a schedule
	s = Schedule()
	s.name = "once a week"
	s.comment = "Schedule for localhost"
	s.first_time = datetime.datetime.today()   # From today
	s.period = datetime.datetime.today()  # At each week NOTE: tmp only
	s.last_time = s.first_time + datetime.timedelta(weeks=42) # For 42 weeks
	s.save()

	# Create a profile
	pro = Profile()
	pro.owner = Owner.objects.get(email="asdf@asdf.com")
	pro.name = "DMZ Servers"
	pro.comment = "Servers: alpha, beta, zeta"
	pro.save()

	# Create a project
	p = Project()
	p.owner = Owner.objects.get(email="asdf@asdf.com")
	p.target.add(t1)
	p.target.add(t2)
	p.schedule = s
	p.description = "test project"
	p.profile = pro
	p.save()

	# Print all objects
	printObjects()
	
	# Delete all created objects
	deleteObjects()

