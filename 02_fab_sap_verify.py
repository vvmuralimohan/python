#! /usr/bin/env python
from fabric.api import env, run, hide, sudo, settings
env.hosts = ['192.168.56.101','192.168.56.102','192.168.56.103','192.168.56.104']
env.user = 'murali'
env.password = 'mohan'

def srvverify():
    with settings(hide('stdout','stderr','output','warnings','running'),warn_only=True):
         result = run('ps -ef | grep ^smaadm | grep -v bash')
         if result.return_code == 0: 
	    for line in result.splitlines():
                print ("Processes still running on %s server with ID." %(env.host))
         else:
	    for line in result.splitlines():
                print ("No processes are running on the %s server." %(env.host))
