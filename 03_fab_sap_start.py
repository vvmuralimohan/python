#! /usr/bin/env python
from fabric.api import env, run, hide, sudo, settings
env.hosts = ['192.168.56.101','192.168.56.102','192.168.56.103','192.168.56.104']
env.user = 'murali'
env.password = 'mohan'

def srvstart():
    with settings(hide('stdout','stderr','output','warnings','running'),warn_only=True):
         result = sudo('/home/smaadm/start.sh', user='smaadm')
         if result.return_code == 0: 
	    for line in result.splitlines():
                print ("Started services successfully on : %s" %(env.host))
         else:
	    for line in result.splitlines():
                print ("Not able to start services on %s server. Due to ERRORS: %s " %(env.host, line))
