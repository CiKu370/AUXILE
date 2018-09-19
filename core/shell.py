##
## main program
##
## written by @ciku370
##

# import modules
import os
import random
from core.parse          import toxic
from core.banner         import *
from core.misc           import *
from core.complete       import *
from modules.webkit      import *
from modules.finder      import *
from modules.encdec      import *
from modules.scanner     import *
from modules.wp_exp      import *
from modules.xssy        import *
from modules.prestashop  import *
from modules.brute       import *
from modules.rce         import rcevuln
from modules.joomsql     import j_sql
from modules.wp_user     import user_scan
from modules.userpro     import check_vuln
from modules.nmap        import nmap_
from core.error          import *
from modules.listener    import listener_

opt = { 'HOST':'127.0.0.1',
        'PORT':'4444' }

def exit_():
    for i in range(random.randrange(1,2)):loading('clean up the framework..')
    printf('\r[+] All done!               ')
    exit()

# shell script
def Fuck_Fake_Friends():
    # banner and auto complete
    banner()
    complete(array)
    # loop forever :v
    while True:
        try:
            an = raw_input('Auxile _> ')
            wibu = an.replace(':','').split()
            # if an == '' or len(wibu) == 0:
            if not wibu:
                pass
            # others
	    elif wibu[0] == 'exec':
		 if len(wibu) == 1:
		     printf('sh: commands not found!',2)
                 os.system(an[2:])
            elif wibu[0] in ['q','quit']:
                exit_()
            elif an == 'help':
                printf(help_)
            elif an == 'modules':
                printf(modules_)
            elif wibu[0] == 'update':
                printf('[+] Checking update..')
                try:
                    os.system('git pull')
                    printf('[w] Please reboot a framework!')
                except:
                    printf('[!] can\'t start update please use <git pull>')
            elif wibu[0] == 'use':
                if len(wibu) == 1:
                    pass
                elif wibu[1] == 'infoga':
                    printf('[+] Load module: modules/%s' % wibu[1])
                    while True:
                       try:
                           an = raw_input('Auxile (\033[93muse modules/infoga\033[0m) _> ')
                           wibu = an.replace(':','').split()
                           arg = toxic(wibu,'-u')
                           if not wibu:
                               pass
                           elif wibu[0] != '-h' and '-h' in wibu or wibu[0] != '--help' and '--help' in wibu:
                               help_menu(wibu[0])
                           elif wibu[0] in webkit_dict:
                               for i in webkit_dict:
                                   if wibu[0] == i:
                                       hackertarget(webkit_dict[i],arg['-u'])
                           elif wibu[0] == 'geoip':
                               geoip(arg['-u'])
                           elif wibu[0] == 'mxrecords':
                               mx(arg['-u'])
                           elif wibu[0] == 'help':
                               show_modules('0')
                           elif wibu[0] in ['q','quit']:
                               break
                       except (IndexError,KeyError):
                           usage(wibu[0])
                       except KeyboardInterrupt:
                           printf('\r\n[!] Interrupt..')
                       except (requests.exceptions.ConnectionError):
                           printf('[!] Connection Error..')
                       except Exception as e:
                           printf('[!] %s' % str(e))
                elif wibu[1] == 'scanners':
                    printf('[+] Load module: modules/%s' % wibu[1])
                    while True:
                        try:
                            an = raw_input('Auxile (\033[93muse modules/scanners\033[0m) _> ')
                            wibu = an.replace(':','').split()
                            arg = toxic(wibu,'-u,-t,-e,-m,-s,--scan')
                            if not wibu:
                                pass
                            elif wibu[0] != '-h' and '-h' in wibu or wibu[0] != '--help' and '--help' in wibu:
                                help_menu(wibu[0])
                            elif wibu[0] == 'port':
                                hackertarget('nmap',arg['-u'])
                            elif wibu[0] == 'nmap':
                                nmap_(arg['-t'],arg['-u'])
                            elif wibu[0] == 'domain_age':
                                domage(arg['-u'])
                            elif wibu[0] == 'default_pass':
                                default_pass(arg['-m'])
                            elif wibu[0] == 'whatcms':
                                cms(arg['-u'])
                            elif wibu[0] == 'subdomain':
                                subdo(arg['-u'])
                            elif wibu[0] == 'honeypot':
                                honey(arg['-u'])
                            elif wibu[0] == 'rce_scan':
                                rcevuln(arg['-u'])
                            elif wibu[0] == 'hackedmail_check':
                                hackedmail(arg['-e'])
                            elif wibu[0] == 'hash_killer':
                                hash_scan()
                            elif wibu[0] == 'dork' and wibu[1] != None:
                                msg = an.replace(wibu[0] + ' ','').replace('-s ','').replace('-s','')
                                if not msg:
                                    usage('dork')
                                elif '-s' in an or '--scan' in wibu:
                                    dorking(msg,'scan')
                                else:
                                    dorking(msg,)
                            elif wibu[0] == 'help':
                                show_modules('1')
                            elif wibu[0] in ['q','quit']:
                                break
                        except (IndexError,KeyError):
                            usage(wibu[0])
                        except KeyboardInterrupt:
                            printf('\r\n[!] Interrupt..')
                        except (requests.exceptions.ConnectionError):
                            printf('[!] Connection Error..')
                        except Exception as e:
                            printf('[!] %s' % str(e))
                elif wibu[1] == 'bruteforce':
                    printf('[+] Load module: modules/%s' % wibu[1])
                    while True:
                        try:
                            an = raw_input('Auxile (\033[93muse modules/bruteforce\033[0m) _> ')
                            wibu = an.replace(':','').split()
                            arg = toxic(wibu,'-u,-s,-w,-i,-f')
                            if not wibu:
			        pass
			    elif wibu[0] != '-h' and '-h' in wibu or wibu[0] != '--help' and '--help' in wibu:
                                help_menu(wibu[0])
  			    elif wibu[0] == 'joom_sql_scan':
				j_sql(arg['-u'])
			    elif wibu[0] == 'wordpress_brute':
                                wordpress(arg['-s'],arg['-u'],arg['-w'])
		            elif wibu[0] == 'ftp_brute':
                		ftp(arg['-i'],arg['-u'],arg['-w'])
		            elif wibu[0] == 'ssh_brute':
                		ssh(arg['-i'],arg['-u'],arg['-w'])
                            elif wibu[0] == 'adfin':
                                adfin(arg['-u'])
                            elif wibu[0] == 'upload':
                                upload(arg['-u'])
                            elif wibu[0] == 'shell':
                                shell(arg['-u'])
                            elif wibu[0] == 'dirscan':
                                dir(arg['-u'])
                            elif wibu[0] == 'xss_scan':
			        xss(arg['-u'])
			    elif wibu[0] == 'lfi_scan':
				lfiscan(arg['-u'])
                            elif wibu[0] == 'help':
                                show_modules('2')
                            elif wibu[0] in ['q','quit']:
                                break
                        except (IndexError,KeyError):
                            usage(wibu[0])
                        except KeyboardInterrupt:
                            printf('\r\n[!] Interrupt..')
                        except (requests.exceptions.ConnectionError):
                            printf('[!] Connection Error..')
                        except Exception as e:
                            printf('[!] %s' % str(e))
                elif wibu[1] == 'exploits':
                    printf('[+] Load module: modules/%s' % wibu[1])
                    while True:
                        try:
                            an = raw_input('Auxile (\033[93muse modules/exploits\033[0m) _> ')
                            wibu = an.replace(':','').split()
                            arg = toxic(wibu,'-u,-n,-f')
                            if not wibu:
                                pass
                            elif wibu[0] != '-h' and '-h' in wibu or wibu[0] != '--help' and '--help' in wibu:
                                help_menu(wibu[0])
                            elif wibu[0] == 'wpscan':
                                wpscan(arg['-u'])
                            elif wibu[0] == 'user_pro':
                                check_vuln(arg['-u'])
                            elif wibu[0] == 'wp_user':
                                user_scan(arg['-u'],arg['-n'])
                            elif wibu[0] == 'wp_sym_exp':
                                exploit_wp(arg['-u'],arg['-f'])
                            elif wibu[0] == 'pres_simple_exp':
                                sss_ex(arg['-u'],arg['-f'])
                            elif wibu[0] == 'pres_product_exp':
                                ppa_ex(arg['-u'],arg['-f'])
                            elif wibu[0] == 'pres_home_exp':
                                hpa_ex(arg['-u'],arg['-f'])
                            elif wibu[0] == 'pres_column_exp':
                                ca_ex(arg['-u'],arg['-f'])
                            elif wibu[0] == 'pres_vtem_exp':
                                vtem_ex(arg['-u'],arg['-f'])
                            elif wibu[0] == 'pres_wizard_exp':
                                awp_ex(arg['-u'],arg['-f'])
                            elif wibu[0] == 'pres_add_exp':
                                aps_ex(arg['-u'],arg['-f'])
                            elif wibu[0] == 'pres_this_exp':
                                atp_ex(arg['-u'],arg['-f'])
                            elif wibu[0] == 'pres_advanced_exp':
                                as_ex(arg['-u'],arg['-f'])
                            elif wibu[0] in ['q','quit']:
                                break
                            elif wibu[0] == 'help':
                                show_modules('3')
                        except (IndexError,KeyError):
                            usage(wibu[0])
                        except KeyboardInterrupt:
                            printf('\r\n[!] Interrupt..')
                        except (requests.exceptions.ConnectionError):
                            printf('[!] Connection Error..')
                        except Exception as e:
                            printf('[!] %s' % str(e))
                elif wibu[1] == 'encryption':
                    printf('[+] Load module: modules/%s' % wibu[1])
                    while True:
                        try:
 			    an = raw_input('Auxile (\033[93muse modules/encryption\033[0m) _> ')
                            wibu = an.replace(':','').split()
                            arg = toxic(wibu,'-s')
                            if not wibu:
                                pass
                            elif wibu[0] != '-h' and '-h' in wibu or wibu[0] != '--help' and '--help' in wibu:
                                help_menu(wibu[0])
			    elif wibu[0] in encdec_array:
                                if '--enc' in wibu or '-e' in wibu:
                                    ende(wibu[0],'enc')
                                elif '--dec' in wibu or '-d' in wibu:
                                    ende(wibu[0],'dec')
                                else:
                                    usage(wibu[0])
                            elif wibu[0] in hash_array:
                                hash(wibu[0],arg['-s'])
			    elif wibu[0] in ['q','quit']:
                                break
                            elif wibu[0] == 'help':
                                show_modules('4')
			except (IndexError,KeyError):
                            usage(wibu[0])
                        except KeyboardInterrupt:
                            printf('\r\n[!] Interrupt..')
                        except (requests.exceptions.ConnectionError):
                            printf('[!] Connection Error..')
                        except Exception as e:
                            printf('[!] %s' % str(e))
                elif wibu[1] == 'RAT':
                    printf('[+] Load module: modules/RAT')
                    while True:
                        try:
                            an = raw_input('Auxile (\033[93muse modules/RAT\033[0m) _> ')
                            wibu = an.replace(':','').split()
                            if not wibu:
                                pass
                            elif wibu[0] == 'help':
                                printf(RAT_)
                            elif wibu[0] == 'set':
                                if len(wibu) == 1:
			            pass
                                elif wibu[1] == 'HOST':
			            printf('[+] Set HOST => %s' % wibu[2])
                                    opt['HOST'] = wibu[2]
				elif wibu[1] == 'PORT':
                                    printf('[+] Set PORT => %s' % wibu[2])
                                    opt['PORT'] = wibu[2]
			    elif wibu[0] == 'show':
			        printf('[+] HOST: %s\n[+] PORT: %s' % (opt['HOST'],opt['PORT']))
			    elif wibu[0] == 'gen':
				printf('[+] Host: %s\n[+] Port: %s' % (opt['HOST'],opt['PORT']))
			        out = open('payload','w')
				out.write(payload_.format(opt['HOST'],opt['PORT']))
				out.close()
				printf('[+] Payload success generated')
			    elif wibu[0] == 'exploit':
				listener_(opt['HOST'],(opt['PORT']))
			    elif wibu[0] in ['q','quit']:
				break
                        except IndexError:
			    pass
                        except KeyboardInterrupt:
                            printf('\r\n[!] Interrupt..')
                        except (requests.exceptions.ConnectionError):
                            printf('[!] Connection Error..')
                        except Exception as e:
                            printf('[!] %s' % str(e))
                else:
                    printf('[!] %s: module not found!' % wibu[1])
            else:
                pass
            # end
        # user interrupt
        except KeyboardInterrupt:
            printf('\r\n[!] Interrupt..')
        # handle error
        except Exception as e:
            printf('[!] %s' % str(e))
# EOF
