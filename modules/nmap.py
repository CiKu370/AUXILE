##
## nmap commands : external
##

from core.error import usage
import os

def nmap(msg):
    os.system('nmap ' + msg)

def nmap_(name,web):
       if name == 'all-cve':
             nmap('-T4 --script http-vuln-* -v %s'%web)
       elif name == 'sqli-scan':
             nmap('-T4 -sV --script http-sql-injection.nse -v %s'%web)
       elif name == 'wordpress':
             nmap('-T4 -sV http-wordpress-* -v %s'%web)
       elif name == 'heartbleed':
             nmap('-d --script ssl-heartbleed.nse --script-args vulns.showall -sV %s'%web)
       elif name == 'ssh-brute':
             nmap('-sV -T4 --script ssh-brute.nse %s -d -v -Pn'%web)
       elif name == 'csrf':
             nmap('-sV -Pn -T4 --script http-csrf.nse -v -d %s'%web)
       elif name == 'webdav-scan':
             nmap('-sV -T4 --script http-webdav-scan.nse -v -d -Pn %s'%web)
       elif name == 'smtp-brute':
             nmap('-sV -T4 --script smtp-brute.nse %s -v'%web)
       else:
	    usage('nmap')
