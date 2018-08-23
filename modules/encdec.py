##
## encryption modules
##
## written by @ciku370
##

from core.misc import printf
import base64
import binascii
import re
import hashlib

encdec_array = ['base16','base32','base64','bin','decimal','hex']
hash_array = ['rot13','rev','md4','md5','sha1','sha224','sha384','sha256','sha512','ripemd160','whirlpool']

def ende(e,i):
     msg = raw_input('\033[92mINPUT\033[0m: String to %sode: ' % i)
     if i == 'enc':
        if e == 'base16':
            printf('[r] Base16 encode: ' + base64.b16encode(msg))
        elif e == 'base32':
            printf('[r] Base32 encode: ' + base64.b32encode(msg))
        elif e == 'base64':
            printf('[r] Base64 encode: ' + base64.b64encode(msg))
        elif e == 'bin':
            printf('[r] Binary: ' + bin(int(binascii.hexlify(msg),16)).replace('b',''))
        elif e == 'decimal':
            printf('[r] Decimal: ' + ''.join([str(ord(c)) for c in msg]))
        elif e == 'hex':
            printf('[r] Hexadecimal: ' + binascii.hexlify(msg))
     elif i == 'dec':
        if e == 'base16':
            printf('[r] Base16 decode: ' + base64.b16decode(msg))
        elif e == 'base32':
            printf('[r] Base32 decode: ' + base64.b32decode(msg))
        elif e == 'base64':
            printf('[r] Base64 decode: ' + base64.b64decode(msg))
        elif e == 'bin':
            printf('[r] String: ' + binascii.unhexlify('%x' % int(msg,2)))
        elif e == 'decimal':
            printf('[r] String: ' + re.sub('1?..', lambda m: chr(int(m.group())),msg))
        elif e == 'hex':
            printf('[r] String: ' + binascii.unhexlify(msg))
     else:
        printf('Usage: %s ( --enc | --dec )'%e)
def hash(name,msg):
    if name == 'rev':
       printf('[r] Reverse string: ' + msg[::-1])
    elif name == 'rot13':
       printf('[r] Rot13: ' + msg[2:].encode('rot13'))
    elif name in ['md4','md5','sha1','sha224','sha256','sha384','sha512','ripemd160','whirlpool']:
       m = hashlib.new(name)
       m.update(msg.encode('utf'))
       printf('[r] %s: %s' % (name,m.hexdigest()))
