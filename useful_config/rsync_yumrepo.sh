

[root@qa0301 rsync_yum_shell]# cat exclude_centos6.list 
SCL/
centosplus/
contrib/
cr/
extras/i386/
fasttrack/
isos/
os/i386/
updates/i386/
xen4/
[root@qa0301 rsync_yum_shell]# cat exclude_centos7.list 
centosplus/
cr/
fasttrack/
isos/
virt/
[root@qa0301 rsync_yum_shell]# 
######


#!/bin/bash
#script name:rsync_yumrepo.sh
RsyncBin="/usr/bin/rsync"
RsyncPerm='-avrt --delete --no-iconv --bwlimit=700'
CentOS_7_base='/data/yum_repo/CentOS_7/'
CentOS_7_epel='/data/yum_repo/CentOS7_Epel/'
CentOS_6_base='/data/yum_repo/CentOS_6/'
CentOS_6_epel='/data/yum_repo/CentOS6_Epel/'
LogFile='/data/yum_repo/rsync_yum_log'
Date=`date +%Y-%m-%d`
#check
function check {
if [ $? -eq 0 ];then
    echo -e "\033[1;32mRsync is success!\033[0m" >>$LogFile/$Date.log
else
    echo -e "\033[1;31mRsync is fail!\033[0m" >>$LogFile/$Date.log
fi
}
if [ ! -d "$CentOS_7_base" ];then
    mkdir -pv $CentOS_7_base
fi
if [ ! -d "$CentOS_7_epel" ];then
    mkdir -pv $CentOS_7_epel
fi
if [ ! -d "$CentOS_6_base" ];then
    mkdir -pv $CentOS_6_base
fi
if [ ! -d "$CentOS_6_epel" ];then
    mkdir -pv $CentOS_6_epel
fi
if [ ! -d "$LogFile" ];then
    mkdir $LogFile
fi
#rsync centos 6 base
echo '$Date Now start to rsync centos 6 base!' >>$LogFile/$Date.log
#$RsyncBin $RsyncPerm --exclude-from=/data/yum_repo/rsync_yum_shell/exclude_centos6.list rsync://mirrors.yun-idc.com/centos/6/ $CentOS_6_base >>$LogFile/$Date.log
$RsyncBin $RsyncPerm --exclude-from=/data/yum_repo/rsync_yum_shell/exclude_centos6.list rsync://mirrors.ustc.edu.cn/centos/6/ $CentOS_6_base >>$LogFile/$Date.log
check
#rsync centos 6 epel
#echo '$Date Now start to rsync centos 6 epel!' >>$LogFile/$Date.log
#$RsyncBin  $RsyncPerm --exclude=SRPMS/ --exclude=ppc64/ --exclude=i386/ rsync://mirrors.yun-idc.com/epel/6/ $CentOS_6_epel  >>$LogFile/$Date.log
$RsyncBin  $RsyncPerm --exclude=SRPMS/ --exclude=ppc64/ --exclude=i386/ rsync://mirrors.ustc.edu.cn/epel/6/ $CentOS_6_epel  >>$LogFile/$Date.log
check
#rsync centos 7 base
echo '$Date Now start to rsync centos 7 base!' >>$LogFile/$Date.log
#$RsyncBin $RsyncPerm --exclude-from=/data/yum_repo/rsync_yum_shell/exclude_centos7.list rsync://mirrors.yun-idc.com/centos/7/ $CentOS_7_base >>$LogFile/$Date.log
$RsyncBin $RsyncPerm --exclude-from=/data/yum_repo/rsync_yum_shell/exclude_centos7.list rsync://mirrors.ustc.edu.cn/centos/7/ $CentOS_7_base >>$LogFile/$Date.log
check
#rsync centos 7 epel
echo '$Date Now start to rsync centos 7 epel!' >>$LogFile/$Date.log
#$RsyncBin $RsyncPerm --exclude=SRPMS/ --exclude=ppc64/ rsync://mirrors.yun-idc.com/epel/7/ $CentOS_7_epel >>$LogFile/$Date.log
$RsyncBin $RsyncPerm --exclude=SRPMS/ --exclude=ppc64/ rsync://mirrors.ustc.edu.cn/epel/7/ $CentOS_7_epel >>$LogFile/$Date.log
check
