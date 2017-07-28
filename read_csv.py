#! /usr/bin/env python
from fabric.api import env, run, hide, sudo, settings, execute
from fabric import tasks
from fabric.network import disconnect_all
import os

env.user = 'murali'
env.password = 'mohan'

# file = open('sids.txt', 'w')

sidfile_array = []

def readfile():
    with open('mysids.txt') as sid_file:
         for line in sid_file:
             currentline = line.split(',')
             sidfile_array.append(currentline)

         for host in sidfile_array:
             print ("Hostname is %s", (host[0]))
             if len(host) > 1:
                for i in range(len(host)-1):
                      print ("SID Admins are %s", (host[i+1]))
             else:
                 print "No SIDs"

def main():
    tasks.execute(readfile)
    disconnect_all()

if __name__ == '__main__':
    main()
