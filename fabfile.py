#! /usr/bin/env python
#def hello():
#        print('Hello world, Tecmint community')
from fabric.api import env, run
#env.hosts = ['192.168.56.101','192.168.56.102','192.168.56.103','192.168.56.104']
env.user = 'murali'
env.password = 'mohan'

def set_hosts():
    env.hosts = open('hosts_file', 'r').readlines()

def uname():
    run("uname -a")

def myuptime():
    run('uptime')
def disk_space():
    run('df -TPh')
def mydisks():
    run('fdisk -l')

# Return the output
#result = sudo("ls -l /var/www")
# Create a directory
#sudo("mkdir /var/www")

# Create a directory as another user
#sudo("mkdir /var/www/web-app-one", user="web-admin")
# Prompt the user with defaults and validation
# port_number = prompt("Which port?", default=42, validate=int)
# Reboot after 30 seconds
# reboot(wait=30)
# The *cd* context manager makes enwrapped command's
# execution relative to the stated path (i.e. "/tmp/trunk")
# with cd("/tmp/trunk"):
#    items = sudo("ls -l")

# It is possible to "chain" context managers
# The run commands gets executed, therefore at "/tmp/trunk"
# with cd("/tmp"):
#    with cd("/trunk"):
#        run("ls")
