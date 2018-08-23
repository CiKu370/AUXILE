##
## error handle and usage modules
##
## written by @ciku370
##

from modules.webkit import *
from modules.encdec import *
from core.misc     import printf

finder_array = ['adfin','upload','shell','dirscan','wpscan','user_pro','lfi_scan','joom_sql_scan','xss_scan','rce_scan']
exp = ['pres_simple_exp','wp_sym_exp','pres_product_exp','pres_home_exp','pres_column_exp','pres_vtem_exp','pres_wizard_exp','pres_add_exp','pres_this_help','pres_advanced_exp']
def hell(text,name,cmd):
    printf('\n[u] ' + str(name) + ' [-h] ' + str(cmd) + '\n\noptional arguments:\n  -h, --help\tshow this help message\n' + text)
def usage(name):
   if name in webkit_dict or name in ['mxrecords','domain_age','whatcms','subdomain','geoip','honeypot']:
      printf('[u] %s [-h] -u HOSTNAME' % name)
   elif name in finder_array:
      printf('[u] %s [-h] -u URL' % name)
   elif name in encdec_array:
      printf('[u] %s [-h] ( --enc | --dec )' % name)
   elif name == 'nmap':
      printf('[u] %s [-h] -t ( all-cve | sqli-scan | wordpress | heartbleed | ssh-brute | csrf | webdav-scan | smtp-brute ) -u <target>' % name)
   elif name in hash_array:
      printf('[u] %s [-h] -s STRING' % name)
   elif name == 'dork':
      printf('[u] %s [-h] [-s] QUERY' % name)
   elif name == 'wp_user':
      printf('[u] %s [-h] -u URL -n NUM' % name)
   elif name == 'hackedmail_check':
      printf('[u] %s [-h] -e EMAIL' % name)
   elif name in exp:
      printf('[u] %s [-h] -u URL -f FILE' % name)
   elif name == 'default_pass':
      printf('[u] %s [-] -m MANUFACTOR' % name)
   elif name == 'wordpress_brute':
      printf('[u] %s [-h] -s URL -u USERNAME -w WORDLIST' % name)
   elif name in ['ssh_brute','ftp_brute']:
      printf('[u] %s [-h] -i HOSTNAME -u USERNAME -w WORDLIST' % name)
def help_menu(name):
    if name in webkit_dict or name in ['mxrecords','domain_age','whatcms','subdomain','geoip','honeypot']:
        hell('  -u HOSTNAME\thostname or domain name\n',name,'-u HOSTNAME')
    elif name in encdec_array:
        hell('  -e, --enc\tencode strings\n  -d, --dec\tdecode strings\n',name,'( --enc | --dec )')
    elif name in finder_array:
        hell('  -u URL\ttarget website\n',name,'-u URL')
    elif name == 'nmap':
        hell('  -u HOSTNAME\thostname or domain name\n  -t TYPE\ttype to be scanned\n',name,'-t ( all-cve | sqli-scan | wordpress | heartbleed | ssh-brute | csrf | webdav-scan | smtp-brute ) -u <target>')
    elif name in hash_array:
        hell('  -s STRING\tthe word will be changed to hash\n',name,'-s STRING')
    elif name == 'dork':
        printf('\n[u] %s [-s] STRING\n\npositional arguments:\n  string\tdork, example: inurl:\'.php?id=\'\n\noptional arguments:\n  -s, --scan\tscan sqli vulnerability\n' % name)
    elif name == 'wp_user':
        hell('  -u URL\ttarget website\n  -n NUM\tnumber of users\n',name,'-u URL')
    elif name in exp:
        hell('  -u URL\ttarget website\n  -f FILE\tfile that will be uploaded\n',name,'-u URL -f FILE')
    elif name == 'default_pass':
        hell('  -m MANUFACTOR\tPassword string\n',name,'-m MANUFACTOR')
    elif name == 'hackedmail_check':
        hell('  -e EMAIL\tYour email will be checked\n',name,'-e EMAIL')
    elif name == 'wordpress_brute':
        hell('  -s URL\ttarget website\n  -u USERNAME\tusername of Wordpress\n  -w WORDLIST\twordlist for attack target\n',name,'-s URL -u USERNAME -w WORDLIST')
    elif name in ['ssh_brute','ftp_brute']:
        xs = name.split('_')[0]
        hell('  -i HOSTNAME\tip address of {xs} server\n  -u USERNAME\tusername of {xs} server\n  -w WORDLIST\twordlist path\n'.format(xs=xs),name,'-i HOSTNAME -u USERNAME -w WORDLIST')
    else:
        printf('%s: not found' % name,2)

