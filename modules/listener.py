##
## listener
##

from core.misc import printf
import socket
def listener_(host,port):
    printf('[+] Listening on port %s' % port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,int(port)))
    s.listen(5)
    c,_ = s.accept()
    printf('[+] Session opened, ip: %s port %s' % (_[0],_[1]))
    while True:
        an = raw_input('Auxile (\033[93mmeterpreter\033[0m) _> ')
        cmd = an.replace(':','').split()
        if not cmd:
	   pass
	else:
	   c.send(cmd)
	   c.recv(10000)
