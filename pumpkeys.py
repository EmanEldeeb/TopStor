#!/bin/python3.6
import sys, subprocess
from etcdput import etcdput as put
from etcdputlocal import etcdput as putlocal
from etcdget import etcdget as get 
from etcddel import etcddel as dels 
from logqueue import queuethis
from logmsg import sendlog
from socket import gethostname as hostname
from sendhost import sendhost
from privthis import privthis 
from time import time as timestamp
from broadcasttolocal import broadcasttolocal
myhost = hostname()
myip = get('ready/'+myhost)[0]
clusterip = get('namespace/mgmtip')[0].split('/')[0]
def pumpkeys(*bargs):
 partnerip = bargs[0]
 replitype = bargs[1]
 repliport = bargs[2]
 phrase = bargs[3]
 cmdline = '/TopStor/preparekeys.sh '+partnerip
 result = subprocess.run(cmdline.split(),stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')[0].replace(' ','_spc_')
 z=['/TopStor/pump.sh','receivekeys.sh',myhost,myip,clusterip, replitype, repliport, phrase, result]
 msg={'req': 'Exchange', 'reply':z}
 print(msg)
 sendhost(partnerip, str(msg),'recvreply',myhost)
 

if __name__=='__main__':
 pumpkeys(*sys.argv[1:])