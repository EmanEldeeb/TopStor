myclusterf='/root/topstorwebetc/mycluster'
mynodef='/root/topstorwebetc/mynode'
mynodedev='enp0s8'
myclusterdev='enp0s8'
data1dev='enp0s8'
data2dev='enp0s8'

#hostname localhost
#echo localhost > /etc/hostname

pkill zfsping 
pkill iscsiwatchdog
pkill topstorrecvrep
pkill syncrequestlooper
pkill fapilooper
#zpool export -a
targetcli clearconfig 
systemctl stop rabbitmq-server

#nmcli conn delete mynode
#nmcli conn delete mycluster
docker stop intdns
docker stop etcd
docker stop httpd
docker stop httpd_local
docker stop flask
docker stop etcdclient 
docker stop rmq 
systemctl stop docker
systemctl stop iscsid 
systemctl stop target 