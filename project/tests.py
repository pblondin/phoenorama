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

from django.test import TestCase
from scanning.models import *
import datetime

class ScanningTest(TestCase):
    def test_simple_project(self):
        p = Project(target="localhost", description="test project #1", create=datetime.datetime.now(), start=datetime.datetime.now(), frequency=datetime.datetime.now())
        p.save()
        
        r = RunningProject(project=p, status="init")
        r.save()
        
        t1 = Tool(name="nmap", config="default")
        t1.save()
        t2 = Tool(name="openvas", config="default")
        t2.save()
        
        task = Task(name="Web", project=p)
        task.save()
        task.tools.add(t1)
        task.tools.add(t2)
        task.save()
        
        #self.failUnlessEqual()
    
    
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)



