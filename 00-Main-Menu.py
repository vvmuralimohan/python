#! /usr/bin/env python
from fabric.api import env, run, hide, sudo, settings, execute
from fabric import tasks
from fabric.network import disconnect_all
import os

env.user = 'murali'
env.password = 'mohan'

file = open('sids.txt', 'w')

def set_hosts():
    env.hosts = open('hosts_file', 'r').readlines()

def getsids():
    with settings(hide('stdout','stderr','output','warnings','running'),warn_only=True):
         result = run("ps -ef | grep -w top | grep -v grep| awk '{print $1}'| sort -u")
         if result.return_code == 0:
            file.write ("\n%s" %(env.host))
            for line in result.splitlines():
                file.write (",%s" %(line))
         else:
            for line in result.splitlines():
                print ("No SIDs on the %s " %(env.host))

def srvstop():
    with settings(hide('stdout','stderr','output','warnings','running'),warn_only=True):
         result = sudo('/home/smaadm/stop.sh', user='smaadm')
         if result.return_code == 0:
            for line in result.splitlines():
                print ("Stopped services successfully on : %s" %(env.host))
         else:
            for line in result.splitlines():
                print ("Not able to stop services on %s server. Due to ERRORS: %s " %(env.host, line))

def srvverify():
    with settings(hide('stdout','stderr','output','warnings','running'),warn_only=True):
         result = run('ps -ef | grep ^smaadm | grep -v bash')
         if result.return_code == 0:
            for line in result.splitlines():
                print ("Processes still running on %s server with ID." %(env.host))
         else:
            for line in result.splitlines():
                print ("No processes are running on the %s server." %(env.host))

def srvstart():
    with settings(hide('stdout','stderr','output','warnings','running'),warn_only=True):
         result = sudo('/home/smaadm/start.sh', user='smaadm')
         if result.return_code == 0:
            for line in result.splitlines():
                print ("Started services successfully on : %s" %(env.host))
         else:
            for line in result.splitlines():
                print ("Not able to start services on %s server. Due to ERRORS: %s " %(env.host, line))
def menu():
          print ("\n  SAP Main Menu to mange services")
          print ("  ===============================")
          print ("\n\t1. Stop Services ")
          print ("\n\t2. Start Services ")
          print ("\n\t3. Verify Services ")
          print ("\n\t4. Verify Services on single server")
          print ("\n\tq. Quit")

def main():
    set_hosts()
    tasks.execute(getsids)
    file.close()
    menu()
    option = raw_input("\nChoose the option : ")
    while option != 'q':
          if option == "1":
             tasks.execute(srvstop)
          elif option == "2":
               tasks.execute(srvstart)
          elif option == "3":
               tasks.execute(srvverify)
          elif option == "4":
               tasks.execute(mygetsid)
          elif option == "q" or option == "Q":
               exit

          print ("Invalid Input.")
          option = raw_input("Choose the option : ")
    disconnect_all()

if __name__ == '__main__':
    main()
