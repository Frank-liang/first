#!/usr/bin/env python
# -*- coding: utf-8 -*-
#修改日期 2014-04-08
#取本机信息，用于ssh登录后显示
import os,time,platform,psutil,urllib,sys,json
import logging,logging.handlers
import socket,fcntl,struct
reload(sys)
sys.setdefaultencoding('utf8')

File = '/etc/motd'
linux_distro = platform.linux_distribution()
share = ' '.join(linux_distro[:2]),platform.system(),platform.architecture()[0],'with',platform.release(),'on',platform.node()
share = ' '.join(share)+'\n'
ignore_fsname = ('', 'cgroup', 'fusectl', 'gvfs-fuse-daemon','gvfsd-fuse', 'none', 'sunrpc')
ignore_fstype = ('autofs', 'binfmt_misc', 'configfs', 'debugfs',
                 'devfs', 'devpts', 'devtmpfs', 'hugetlbfs',
                 'iso9660', 'linprocfs', 'mqueue', 'none',
                 'proc', 'procfs', 'pstore', 'rootfs',
                 'securityfs', 'sysfs', 'usbfs')
ignore_mntpoint = ('', '/dev/shm', '/lib/init/rw', '/sys/fs/cgroup','/boot')

def get_ip(name):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', name[:15]))
        ret = socket.inet_ntoa(inet[20:24])
        return ret
    except Exception , e:
        return None

def write_motd(msg):
    #print msg
    if os.path.isfile(File):
        try:
            f = open(File,'a+')
            f.write(msg)
        except Exception , e:
            print e
        finally:
            f.close()
    else:
        os.popen('touch %s'%(File))

def G_M_K(item):
    item = float(item)
    if item/1024/1024/1024 > 1:
        return '%.2f G'%(item/1024/1024/1024)
    elif item/1024/1024 > 1:
        return '%.2f M'%(item/1024/1024)
    elif item/1024 > 1:
        return '%.2f K'%(item/1024)
    else:return  '%.2f '%(item)

def disk():
    write_motd('\t本机磁盘:\n')
    fs_list = []
    fs_stat = psutil.disk_partitions(all=True)
    for fs in range(len(fs_stat)):
        if fs_stat[fs].device not in ignore_fsname and fs_stat[fs].fstype not in ignore_fstype and fs_stat[fs].mountpoint not in ignore_mntpoint:
            try:
                fs_usage = psutil.disk_usage(fs_stat[fs].mountpoint)
                #fs_list.append('设备名: '+fs_stat[fs].device+'\t'+'挂载点:'+fs_stat[fs].mountpoint)
                fs_list.append('挂载点:'+fs_stat[fs].mountpoint)
                fs_list.append('总大小:'+str(G_M_K(fs_usage.total)))
                fs_list.append('已使用:'+str(G_M_K(fs_usage.used)))
                fs_list.append('可使用:'+str(G_M_K(fs_usage.free)))
                fs_list.append('使用率:'+str(fs_usage.percent)+'%')
                write_motd('\t\t\t'+'\t'.join(fs_list)+'\n')
                fs_list = []
            except Exception , e:
                print e
def load():
    getload = os.getloadavg()
    load = ['\t本机load:\n','\t\t\t一分钟:',str(getload[0]),'五分钟:',str(getload[1]),'十五分钟:',str(getload[2])]
    load = ' '.join(load)
    write_motd(load+'\n')
def mem():
    write_motd('\t本机内存:\n')
    phymem = psutil.virtual_memory()
    total = phymem.total
    free = phymem.available  # phymem.free + buffers + cached
    used = total - free
    mem = []
    mem.append('总大小:'+str( G_M_K(total) ))
    mem.append('空闲内存:'+str( G_M_K(free) ))
    mem.append('内存使用:'+str( G_M_K(used) ))
    write_motd( '\t\t\t'+'\t\t'.join(mem)+'\n')
def swap():
    virtmem = psutil.swap_memory()
    write_motd('\t本机swap:\n')
    swap = []
    swap.append('总大小:'+str(G_M_K(virtmem.total)))
    swap.append('空闲swap:'+str(G_M_K(virtmem.free)))
    swap.append('swap使用:'+str(G_M_K(virtmem.used)))
    write_motd('\t\t\t'+'\t\t'.join(swap)+'\n')
def eths_and_io():
    network_old = psutil.network_io_counters(pernic=True)
    diskio_old = psutil.disk_io_counters(perdisk=True)
    time.sleep(0.5)
    network_new = psutil.network_io_counters(pernic=True)
    diskio_new = psutil.disk_io_counters(perdisk=True)
    eth = ['\n\t网卡信息:\t(全部取 0.5 秒的瞬时值)\n']
    for net in network_new:
        eth.append('\t\t\t'+net)
        eth.append('\t\t\tRX : '+str( G_M_K(network_new[net].bytes_recv - network_old[net].bytes_recv) ))
        eth.append('\t\t\tTX : '+str( G_M_K(network_new[net].bytes_sent - network_old[net].bytes_sent) )+'\n')
    write_motd(''.join(eth)+'\n')
    d = ['\t磁盘IO:\n']
    for disk in diskio_new:
        d.append('\t\t\t'+disk)
        d.append('\t\t\tRead_bytes : '+str( G_M_K(diskio_new[disk].read_bytes - diskio_old[disk].read_bytes) ))
        d.append('\t\t\tWrite_bytes : '+str( G_M_K(diskio_new[disk].write_bytes - diskio_old[disk].write_bytes) )+'\n')
    write_motd(''.join(d)+'\n')
def search(ClientIp):
    SearchIp = "http://ip.taobao.com/service/getIpInfo.php?ip=%s"%(ClientIp)
    try:
        req = urllib.urlopen(SearchIp)
        req = json.loads(req.readlines()[0])
        if "data" in req:
            req = req["data"]
        write_motd("Client Ip: %s\tcountry(%s) area(%s) region(%s) city(%s) isp(%s)\n"%(req["ip"],req["country"],req["area"],req["region"],req["city"],req["isp"]))
    except Exception,e:
        pass

def main():
    tmp = ['本机IP:']
    for e in psutil.network_io_counters(pernic=True):
        if e <> 'lo':
            Ip = str(get_ip(e))
            if "None" not in Ip:
                tmp.append(Ip)
    write_motd(share)
    write_motd('\t'+'\t'.join(tmp)+'\n')
    load()
    disk()
    mem()
    swap()
    eths_and_io()
if __name__ == '__main__':
    os.popen('echo "" >'+File)
    #main()
    if sys.argv[1]:
        search(sys.argv[1])
    main()

