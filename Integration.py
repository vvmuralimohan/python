
#! /usr/bin/env python
from fabric.api import env, run, hide, sudo, settings, execute
from fabric import tasks
from fabric.network import disconnect_all
import os

env.user = 'murali'
env.password = 'mohan'

sidfile_array = []

def readfile():
    with open('mysids.txt') as sid_file:
         for line in sid_file:
             line = line.rstrip('\n')
             currentline = line.split(',')
             sidfile_array.append(currentline)

         for host in sidfile_array:
             print ("\nHostname: %s" %(host[0]))
             if len(host) > 1:
                for i in range(len(host)-1):
#                      with settings(host_string=host[0],warn_only=True,hide('stdout','stderr','output','warnings','running')):
                      with settings(hide('stdout','stderr','output','warnings','running'),host_string=host[0],warn_only=True):
                           USER=(host[i+1])
                           result = sudo("/home/%s/stop.sh" %USER, user=(USER))
                           if result.return_code == 0:
                              for line in result.splitlines():
                                  print ("Instance %s stopped successfully on %s" %(USER,host[0]))
                           else:
                                print ("Not able to execute /home/%s/stop/sh script on the server." %(USER))
                               
             else:
                 print "No SIDs"

def main():
    tasks.execute(readfile)
    disconnect_all()

if __name__ == '__main__':
    main()
