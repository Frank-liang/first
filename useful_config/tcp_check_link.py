#!/usr/bin/python
# coding:utf-8
from itertools import dropwhile

sys_st = {
    "00": "ERROR_STATUS",
    "01": "TCP_ESTABLISHED",
    "02": "TCP_SYN_SENT",
    "03": "TCP_SYN_RECV",
    "04": "TCP_FIN_WAIT1",
    "05": "TCP_FIN_WAIT2",
    "06": "TCP_TIME_WAIT",
    "07": "TCP_CLOSE",
    "08": "TCP_CLOSE_WAIT",
    "09": "TCP_LAST_ACK",
    "0A": "TCP_LISTEN",
    "0B": "TCP_CLOSING",
}

tcp_static_dict = {}

with open("/proc/net/tcp") as f:
    for line in dropwhile(lambda line: line.strip().startswith('sl'), f):
        tcp_status_code = line.split()[3]
        if sys_st.has_key(tcp_status_code):
            if tcp_static_dict.get(sys_st[tcp_status_code], None) is None:
                tcp_static_dict[sys_st[tcp_status_code]] = 1
            else:
                tcp_static_dict[sys_st[tcp_status_code]] += 1
print tcp_static_dict
