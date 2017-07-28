#! /usr/bin/env python
from fabric.api import env, run, local, hide, sudo, settings, execute
from fabric import tasks
from fabric.network import disconnect_all

import os
# import sys

env.user = 'murali'
env.password = 'mohan'
# env.hosts = ['192.168.56.101','192.168.56.102','192.168.56.103','192.168.56.104']

file = open('sids.txt', 'w')


def set_hosts():
    env.hosts = open('hosts_file', 'r').readlines()

def uname():
    run("uname -a")

def getsids():
    with settings(hide('stdout','stderr','output','warnings','running'),warn_only=True):
         result = run("ps -ef | grep -w top | grep -v grep| awk '{print $1}'| sort -u")
         if result.return_code == 0: 
            print ("SIDs on  : %s" %(env.host))
            file.write ("%s" %(env.host))
	    for line in result.splitlines():
                print ("SID : %s" %(line))
                file.write (",%s" %(line))
         else:
	    for line in result.splitlines():
                print ("No SIDs on the %s " %(env.host))

def hosts():
#    result = sudo("ps -ef | grep -w top | grep -v grep| awk '{print $1}'| sort -u")
    print ("SIDs on  : %s"  %(env.host))

def main():
#    getsids()
    print ("Before set hosts")
    set_hosts()
    print ("After set hosts")
    uname()
    disconnect_all()

if __name__ == '__main__':
    main()
