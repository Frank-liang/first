#!/bin/bash
#用户登录显示系统信息
file="/etc/motd"
ClientIp=`who am i | awk '{print $5}' | sed 's/(//g' | sed 's/)//g'`
check () {
ip=`ifconfig |grep "inet addr"|awk '{print $2}'|awk -F: '{print $2}'|head -n 1`
echo "系统信息：" > $file
echo "    `uname -a`" >> $file
echo "    本机IP: $ip" >> $file
echo "    本机host: `hostname`" >> $file
echo -e "\t\t总大小\t已使用\t剩余\t使用%\t挂载点\t\t设备" >> $file
for i in $(seq `df -Ph|grep /|wc -l`);do
echo "    `df -Ph|grep /|tail -n +$i |head -n 1|awk '{print "\t\t"$2,"\t"$3,"\t"$4,"\t"$5,"\t"$6,"\t\t"$1 }'`" >> $file
done
}
ip=`who -u am i 2>/dev/null| awk '{print $NF}'|sed -e 's/[()]//g'`
echo "" > $file
/opt/Python-2.7.3/bin/python /etc/use_login.py "$ClientIp"
if [ "$?" -ne "0" ];then
    check
fi

