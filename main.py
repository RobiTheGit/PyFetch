#!/usr/bin/python3
import sys
import os
import psutil
os_release = open('/etc/os-release', 'r')
prettyname0 = os_release.readline()
OTP_prettyname = prettyname0.split('=')
PrettyName = ((OTP_prettyname[1]).replace('"', '')).replace('\n', '')
os_release.close()
mem = psutil.virtual_memory()
print(os.getlogin() + '@' + os.uname().nodename)
print('OS:', PrettyName, os.uname().machine)
print('CPU Cores:',os.cpu_count())
print('Kernel:', os.uname().release)
print('Memory:', mem.active, '/', mem.total) 
