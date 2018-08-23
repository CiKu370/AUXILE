##! usr/bin/python2.7
## coding: utf-8
##
## banner
##
## written by @ciku370
##

from core.misc import printf
import time
import sys
import random

def loading(text):
    num = 0
    while num < 1:
        for i,char in enumerate(text):
            if i == 0:
                print "\r%s%s" %(char.upper(),text[1:]),
                sys.stdout.flush()
            elif i == 1:
                old_text = text[0].lower()
                print "\r%s%s%s" %(old_text,char.upper(),text[2:]),
                sys.stdout.flush()
            elif i == i:
                old_text = text[-0:i].lower()
                print "\r%s%s%s" %(old_text,char.upper(),text[i+1:]),
                sys.stdout.flush()
            time.sleep(0.1)
        num += 1
def tests_pyver():
    if sys.version[:3] == "2.7" or "2" in sys.version[:3]:
        pass
    elif "3" in sys.version[:3]:
        printf("\r[i] Auxile has no support for Python 3.x")
    else:
        printf("\r[w] Your Python version is very old ..")

def tests_platform():
    if sys.platform not in ['linux','linux2','darwin','win']:
        printf("\r[w] If \'Auxile\' run sucsessfuly on your platform %s\nPlease let me (@CiKu370) know!" %sys.platform)
def banner():
    try:
        sys.stdout.write("\x1b]2;Auxile Framework - @CiKu370\x07")
        for i in range(random.randrange(1,2)):loading("Loading the fingerprinting framework..")
        tests_pyver()
        tests_platform()
        printf('''\r[w] If you don't know how run it use help !\033[92m

    ▄████████ ███    █▄ ▀████    ▐████▀  ▄█   ▄█        ▄████████
   ███    ███ ███    ███  ███▌   ████▀  ███  ███       ███    ███
   ███    ███ ███    ███   ███  ▐███    ███▌ ███       ███    █▀
   ███    ███ ███    ███   ▀███▄███▀    ███▌ ███      ▄███▄▄▄
 ▀███████████ ███    ███   ████▀██▄     ███▌ ███     ▀▀███▀▀▀
   ███    ███ ███    ███  ▐███  ▀███    ███  ███       ███    █▄
   ███    ███ ███    ███ ▄███     ███▄  ███  ███▌    ▄ ███    ███
   ███    █▀  ████████▀ ████       ███▄ █▀   █████▄▄██ ██████████\033[0m
                       Coded by @CiKu370
''')
    except KeyboardInterrupt:
        print('\n\033[91mERROR\033[0m: Interrupt..')
        exit()
