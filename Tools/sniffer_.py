
"""
The first part of code > Sniffer CyberSI
ROOT? SUDO?
Varios modulos sem implementar ALPHAAAA
"""

__author__ = "x86_g"
__copyright__ = "None"
__credits__ = ["x86_g"]
__license__ = "Free"
__version__ = "0.0.1 (Alpha)"
__maintainer__ = "x86_g"
__email__ = "pedro.secinfo@gmail.com"
__status__ = "Alpha/Test"
__url__ = "https://github.com/area31/CYBER-SI"

import	socket

START = "\x1b["
GREEN =  "32m"
RED = "31m"
YELLOW = "33m"
BLUE = "34m"
PURPLE = "35m"
BOLD = "01;"
UNDERLINE = "04;"
RESET = "\x1b[00m"

SUCCESS = START+BOLD+GREEN
FAILURE = START+BOLD+RED
UNKNOWN = START+BOLD+YELLOW
TITLE = START+BOLD+UNDERLINE+PURPLE
MESSAGE = START+BOLD+BLUE


class SECURE():
    TOTAL_SECURE = 0
    TOTAL_UNSECURE = 0
    TOTAL_UNKNOWN = 0
    content = ""
    
    def __init__(self):
        self.is_root()
        
    def write_header(self):
        sys.stdout.write("%sCyberSI Sniffer%s - %s%s" % (MESSAGE, __version__, __url__, RESET))
        sys.stdout.write("\n\n")
        sys.stdout.write("A SNIFFER")
        sys.stdout.write("\n\n")
        sys.stdout.write("%sSniffing your Traffic! ...%s" % (SUCCESS, RESET))
        sys.stdout.write("\n\n")
        
    def write_footer(self):
        sys.stdout.write("%s... Done%s" % (SUCCESS, RESET))
        sys.stdout.write("\n\n")
        self.totals()

    def is_root(self):
        """Check if user is super user"""
        if os.geteuid() == 0:
            return True
        sys.stdout.write("You need to be a superuser to run this program\n")
        sys.exit(os.EX_NOUSER)
sniffa = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

#PEGA PACOTES 
while True:
	print sniffa.recvfrom(65565)

for sniffado in sniffa.stdout:
    if "!BBHHHBBH4s4s" in sniffa:
        print ("[+]"+str(sniffado.rstrip()[21:]))

    if IP[0:12] in sniffado:
        print ("YOU==>"+str(sniffa.rstrip()))



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Sniffer parado!'
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

