x#!/usr/bin/python3
import subprocess,sys
from ast import literal_eval as mtuple
from etcdgetpy import etcdget as getp
from etcdgetlocalpy import etcdget as get
from etcdputlocal import etcdputlocal


thehost=sys.argv[1]
key=sys.argv[2]
tokey=sys.argv[3]
leaderip = get('leaderip')
result=getp(leaderip, key,'--prefix')
print("the result",result)
if result==[]:
 print('_1')
 exit(1)
for item in result:
 x=item[0].replace('/','')
 x=x.replace(str(key),'')
 if x =='':
   adding='';
 else:
   adding='/'+x
 etcdputlocal(tokey+adding, item[1])
