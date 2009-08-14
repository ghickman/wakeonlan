#!/usr/bin/env python
import re, socket
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-i', '--ip', dest='ip', help='The ip address to broadcast your ip address on')
parser.add_option('-m', '--mac', dest='mac', help='The MAC address of the target machine')
(options, args) = parser.parse_args()

options.mac = '12-34-56-78-90:ab'
if len(options.mac) < 17 or not re.compile('([a-fA-F0-9]{2}[:\-]?){6}').match(options.mac): raise Exception('MAC address not in the correct format')

mac = options.mac.replace(':','\\x').replace('-','\\x')

#s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.sendto('\xff'*6+options.mac*16, (options.ip, 80))
