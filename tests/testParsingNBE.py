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
Created on Mar 22, 2011

@author: r00tmac
'''
import re, csv

class Parser():
    '''
    A parser for NBE (OpenVAS, Nessus) to convert into our RESULT model. 
    '''
    
    def __init__(self):
        self.result = [[]]

    
    def parse(self, nbe_file):
        try:
            whole_file = csv.reader(open(nbe_file, 'rb'), delimiter='|')
            for row in whole_file:
                if len(row) == 0:
                    pass
                else:
                    if row[0] == "results":
                        if len(row) > 4:
                            (service, port, protocol) = self.__parserow3(row[3])
                            target = row[2]       
                            severity = self.__getrisklevel(row[5], row[6])
                            data = row[6]
                            nvtoid = row[4]
                            if nvtoid == '':
                                print "Open PORT"
                                classification = "Open port: " + row[3]
                                cve_id = []
                                bugtraq_id = []
                                summary = classification
                            else:   
                                pass                             
                                '''infos = self.getnvtinfos(doc, nvtoid)
                                if len(infos) != 0:
                                    classification = infos['name']
                                    cve_id = infos['cve_id'].split(',')
                                    bugtraq_id = infos['bugtraq_id'].split(',')
                                    summary = infos['summary']'''
                            self.result.append([service, port, protocol, target, severity, data, nvtoid])
                                
        except IOError, msg:
            print (str(msg))

    #############################################
    # Private methods for parsing
    #############################################
    def __splitonslash(self, string):
        string = re.sub("\(", "", string)
        string = re.sub("\)", "", string)
        (key1, key2) = string.split("/",1)
        return key1, key2

    def __parserow3(self, list):
        tmprow3 = list.split(" ",1)
        if len(tmprow3) > 1:
            (port, protocol) = self.__splitonslash(tmprow3[1])
            service = tmprow3[0]
        else:
            (service, protocol) = self.__splitonslash(tmprow3[0])
            port = "0"
        return service, port, protocol

    def __getrisklevel(self, risk, value):
        result = ""
        if risk == "Security Hole":
            result = "high"
        elif risk == "Security Warning":
            match = re.search("Risk factor\W+(\w+)", value)
            if match:
                tmpmatch = match.group(1).lower().strip()
                if tmpmatch == "medium" or tmpmatch == "high":
                    result = "medium"
                else:
                    result = "low"
            else:
                result = "low"
        elif risk == "Log Message" or risk == "Security Note":
            result = "info"
        return result

    def __getnvtinfos(self, xmldoc, nvtoid):
        infos = {}
        expr = "/openvas-report/nvts/nvt[@oid = $nvt]/*"
        for ele in xmldoc.xpath(expr, nvt = nvtoid):
            infos[ele.tag] = ele.text
        return infos


if __name__ == '__main__':
    nbe_input = '22-09-2010.nbe'
    
    p = Parser()
    p.parse(nbe_input)
    
    
    for r in p.result:
        print r
    #print nbe_input




