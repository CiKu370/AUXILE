##
## scanner modules
##
## Credit to (https://github.com/s0md3v/Hash-Buster/blob/master/hash.py)
##

from core.misc import printf
from re        import search
from bs4       import BeautifulSoup
import cookielib
import random
import urllib2
import re
import requests

errors = {'MySQL': 'error in your SQL syntax',
             'MiscError': 'mysql_fetch',
             'MiscError2': 'num_rows',
             'Oracle': 'ORA-01756',
             'JDBC_CFM': 'Error Executing Database Query',
             'JDBC_CFM2': 'SQLServer JDBC Driver',
             'MSSQL_OLEdb': 'Microsoft OLE DB Provider for SQL Server',
             'MSSQL_Uqm': 'Unclosed quotation mark',
             'MS-Access_ODBC': 'ODBC Microsoft Access Driver',
             'MS-Access_JETdb': 'Microsoft JET Database',
             'Error Occurred While Processing Request' : 'Error Occurred While Processing Request',
             'Server Error' : 'Server Error',
             'Microsoft OLE DB Provider for ODBC Drivers error' : 'Microsoft OLE DB Provider for ODBC Drivers error',
             'Invalid Querystring' : 'Invalid Querystring',
             'OLE DB Provider for ODBC' : 'OLE DB Provider for ODBC',
             'VBScript Runtime' : 'VBScript Runtime',
             'ADODB.Field' : 'ADODB.Field',
             'BOF or EOF' : 'BOF or EOF',
             'ADODB.Command' : 'ADODB.Command',
             'JET Database' : 'JET Database',
             'mysql_fetch_array()' : 'mysql_fetch_array()',
             'Syntax error' : 'Syntax error',
             'mysql_numrows()' : 'mysql_numrows()',
             'GetArray()' : 'GetArray()',
             'FetchRow()' : 'FetchRow()',
             'Input string was not in a correct format' : 'Input string was not in a correct format',
             'Not found' : 'Not found'}

def hash_scan():
     hash = raw_input('\033[92mINPUT\033[0m: Enter hash: ')
     if hash == None and len(hash) not in [32,40,64,96]:
        printf('[!] Invalid hash',2)
     response = requests.get('https://lea.kz/api/hash/' + hash).text
     match = search(r': "(.*?)"', response)
     if match:
         printf('[+] Hashed string: ' + match.group(1))
     else:
         data = {'md5' : hash, 'x' : '21', 'y' : '8'}
         response = requests.post('http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php', data).text
         match = search(r'<span class=\'middle_title\'>Hashed string</span>: [^<]*</div>', response)
         if match:
             printf('[+] Hashed string: ' + match.group(1))
         else:
             if len(hash) == 32:
                 response = requests.get('http://www.nitrxgen.net/md5db/' + hash).text
                 if len(response) > 0:
                     printf('[+] Hashed string: ' + response)
                 else:
                     r = requests.get('https://hashtoolkit.com/reverse-md5-hash/'+hash)
                     match = search(r'<span title="decrypted md5 hash">(.*?)</span>',r.text)
                     if match:
                         printf('[+] Hashed string: ' + match.group(1))
                     else:
                         r = requests.get('https://md5.gromweb.com/?md5='+hash)
                         match = search(r'<em class="long-content string">(.*?)</em></p>',r.text)
                         if match:
                             printf('[+] Hashed string: ' + match.group(1))
                         else:
                             printf('[!] String not found!')
             elif len(hash) == 40:
                 data = {'auth':'8272hgt', 'hash':hash, 'string':'','Submit':'Submit'}
                 response = requests.post('http://hashcrack.com/index.php' , data).text
                 match = search(r'<span class=hervorheb2>(.*?)</span></div></TD>', response)
                 if match:
                     printf('[+] Hashed string: ' + match.group(1))
                 else:
                     r = requests.post('https://sha1.gromweb.com/?hash='+hash)
                     match = search(r'<em class="long-content string">(.*?)</em></p>',r.text)
                     if match:
                         printf('[+] Hashed string: ' +  match.group(1))
                     else:
                         printf('[!] String not found!')
             elif len(hash) == 64:
                 response = requests.get('http://md5decrypt.net/Api/api.php?hash=%s&hash_type=sha256&email=deanna_abshire@proxymail.eu&code=1152464b80a61728' % hash).text
                 if len(response) != 0:
                     printf('[+] Hashed string: ' + response)
                 else:
		     r = requests.get('https://hashtoolkit.com/reverse-sha256-hash/' + hash)
		     match = search(r'<span title="decrypted sha256 hash">(.*?)</span>',r.text)
		     if match:
			 printf('[+] Hashed string: ' + match.group(1))
		     else:
                         printf('[!] String not found!')
	     elif len(hash) == 96:
                 r = requests.get('http://hashtoolkit.com/decrypt-sha384-hash/' + hash)
		 match = search(r'<span title="decrypted sha384 hash">(.*?)</span>',r.text)
                 if match:
		     printf('[+] Hashed string:' + match.group(1))
                 else:
                     printf('[!] String not found!')
             else:
                printf('[!] hash not supported')
def dorking(query , sqlscan = None):
    printf('[+] Start dorking..')
    headers = { 'User-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36' }
    urls = []
    FILE = 'Auxile_dork_result.txt'
    out = open(FILE,'w')
    # google.com
    printf('[+] Fetching url from Google..')
    for i in range(1,5):
        payload = { 'q' : query , 'start' : i }
        req = requests.get(
                'http://www.google.com/search',
                payload,
                headers = headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        h3tags = soup.find_all('h3', class_='r')
        for h3 in h3tags:
            try:
                urls.append(re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1))
            except:continue
    # bing.com
    printf('[+] Fetching url from Bing..')
    for i in range(1,5):
        payload = { 'q' : query , 'first' : i }
        req = requests.get(
                'https://www.bing.com/search',
                payload,
                headers = headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        h3tags = soup.find_all('li', class_='b_algo')
        for h3 in h3tags:
            urls.append(h3.find('a').attrs['href'])
    # yahoo.com
    printf('[+] Fetching url from Yahoo..')
    for i in range(1,5):
        payload = { 'p' : query , 'pstart' : i }
        req = requests.get(
                'https://search.yahoo.com/search',
                payload,
                headers = headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        for i in soup.find_all('a'):
            if 'yahoo' not in i.attrs['href'] and 'javascript' not in i.attrs['href'] and '#' not in i.attrs['href']:
                urls.append(i.attrs['href'])
    # dogpile.com
    printf('[+] Fetching url from Dogpile..')
    payload = { 'q' : query }
    req = requests.get(
            'http://results.dogpile.com/search/web',
            payload,
            headers = headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    for i in soup.find_all('a', class_='title'):
        if '/serp?' not in i.attrs['href'] :
            urls.append(i.attrs['href'])
    # aol.com
    printf('[+] Fetching url from AOL..')
    payload = { 'q' : query }
    req = requests.get(
            'https://search.aol.com/aol/search',
            payload,
            headers = headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    for i in soup.find_all('a'):
        if 'aol' not in i.attrs['href'] and '#' not in i.attrs['href']and 'ebay' not in i.attrs['href'] and 'policies' not in i.attrs['href']:
            urls.append(i.attrs['href'])
    # ask.com
    printf('[+] Fetching url from Ask..')
    for i in range(1,5):
        payload = { 'q' : query , 'page' : 2 }
        req = requests.get(
                'http://www.search.ask.com/web',
                payload,
                headers = headers)
        soup = BeautifulSoup( req.text, 'html.parser' )
        for i in soup.find_all('a' , class_='algo-title'):
            if '/serp?' not in i.attrs['href'] :
                urls.append(i.attrs['href'])
    # webcrawler.com
    printf('[+] Fetching url from WebCrawler..')
    payload = { 'q' : query }
    req = requests.get(
            'http://www.webcrawler.com/serp',
            payload,
            headers = headers)
    soup = BeautifulSoup( req.text, 'html.parser' )
    for i in soup.find_all('a', class_='web-bing__title'):
        if '/serp?' not in i.attrs['href'] :
            urls.append(i.attrs['href'])
    # info.com
    printf('[+] Fetching url from Info..')
    payload = { 'q' : query }
    req = requests.get(
          'http://www.info.com/serp',
          payload,
          headers = headers)
    soup = BeautifulSoup( req.text, 'html.parser' )
    for i in soup.find_all('a', class_='web-bing__title'):
        if '/serp?' not in i.attrs['href'] :
            urls.append(i.attrs['href'])
    # infospace.com
    printf('[+] Fetching url from InfoSpace..')
    payload = { 'q' : query }
    req = requests.get(
          'http://search.infospace.com/search/web',
          payload,
          headers = headers)
    soup = BeautifulSoup( req.text, 'html.parser' )
    for i in soup.find_all('a', class_='title'):
        if '/serp?' not in i.attrs['href'] :
            urls.append(i.attrs['href'])
    if len(urls) == 0:
        printf('[!] Could not find anything !')
        return
    if sqlscan == None:
        for i in urls:
            out.write(i.replace('%3F','?').replace('%3D','=') + '\n')
        out.close()
        printf('[+] Found %s urls, output file: %s' % (len(urls),FILE))
    else:
        debby = []
        printf('[+] Scan sql error..')
        outsql = open('Auxile_sql_result.txt','w')
        for i in urls:
            try:
                url = i.replace('%3F','?').replace('%3D','=')
                source = requests.get(url + "'").text
                for type,eMSG in errors.items():
                    if re.search(eMSG, source):
			printf('*? %s [\033[92m%s\033[0m]' % (url,type))
                        debby.append(url)
            except:
                pass
        if len(debby) == 0:
            printf('[!] Can\'t find sql error !')
            return
	else:
            for i in debby:
		outsql.write(i.strip() + '\n')
	    outsql.close()
            printf('[+] Found %s urls, output file: Auxile_sql_result.txt' % debby)
def hackedmail(email):
    headers = {'User-Agent': 'Mozilla/5.0 (X11;Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}
    printf('[+] Try loading email: %s' % email)
    req = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/{}'.format(email), headers=headers, verify=True)
    if len(req.content) == 0:
        printf('[+] No pwnage found')
    else:
        printf('[w] Email: %s' % email)
        printf('[w] Breaches you were pwned in.')
        json_loads = json.loads(req.content.decode('ascii', 'ignore'))
        for i, item in enumerate(json_loads):
            printf('\n[+] %s\n[+] Domain: %s\n[+] Date: %s\n[+] Frabricated: %s\n[+] Verified: %s\n[+] Retired: %s\n[+] Spam: %s\n' % (item['Title'],item['Domain'], item['BreachDate'],item['IsFabricated'], item['IsVerified'], item['IsRetired'], item['IsSpamList']))
        printf('[+] Pwned on %s breached!' % i+1)
def default_pass(manufactor):
    x = {}
    search_link = "http://www.defaultpassword.com/?action=dpl&char="+manufactor
    printf('[+] Searching for passwords.')
    req = requests.get(search_link)
    html = req.content
    result = html.split('<TR VALIGN="top">')
    try:
        result.pop(0)
        result.pop(0)
        for line in result:
            spliting = line.split('<TD NOWRAP>')
            string = ''
            for element in spliting:
                if "</TD>" in element and element.strip() != '':
                    manufactor = spliting[1].split('</TD>')[0]
                    product = spliting[2].split('</TD>')[0]
                    protocol = spliting[4].split('</TD>')[0]
                    user = spliting[5].split('</TD>')[0]
                    password = spliting[6].split('</TD>')[0]
            printf('[+] Manufactor: %s\n[+] Product: %s\n[+] Protocol: %s\n[+] User: %s\n[+] Password: %s' % (manufactor,product,protocol,user,password))
    except IndexError:
        printf('[w] No results were found for this manufacturer.')
