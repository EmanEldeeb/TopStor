#!/usr/bin/python3
import subprocess,sys
from etcdgetpy import etcdget as getp
from etcdgetlocalpy import etcdget as get
from ast import literal_eval as mtuple
from etcdputlocal import etcdput as putlocal 
from etcddellocal import etcddel as dellocal 


thehost=sys.argv[1]
key=sys.argv[2]
tokey=sys.argv[3]
print('thehost',thehost,tokey)
leaderip = get('leaderip')
mylist=getp(leaderip,key,'--prefix')
dellocal(thehost,tokey,'--prefix')

print('mylist:',mylist)
if '_1' in mylist:
 print('_1')
 exit()
for item in mylist:
 moditem=""
 restitem=""
# if '/' in item[0]:
#  moditem=item[0].split('/')[0]
#  restitem='/'+item[0].replace(moditem+'/','')
 keysplit=item[0].split(key)
 if len(keysplit) > 1:
  restitem=keysplit[1]
 putlocal(tokey+restitem, item[1])
 
