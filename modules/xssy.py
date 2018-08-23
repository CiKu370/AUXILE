##
## xss payload scanner
##

import requests
from core.misc import printf

def xss(web):
    vuln = 0
    payloads = open('core/wordlist/xss.txt')
    if 'http' not in web:
        try:
            requests.get('http://' + web)
            url = 'http://' + web
        except:
            url = 'https://' + web
    else:
        url = web
    if '=' in url:
        printtf('[+] Scanning (%s)' % url)
        r = requests.get(url)
        content = r.text
        for payload in payloads:
            if payload.strip().lower() in content.lower():
                print(" XSS Vulnerable: " +url + payload)
                vuln += 1
        if len(vuln) == 0:
            print "[!] Not vulnerable!"
    else:
        printf('[!] No parameter found!')
