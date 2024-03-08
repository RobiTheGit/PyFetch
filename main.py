#!/usr/bin/python3
import sys
import os
import psutil
os_release = open('/etc/os-release', 'r')
prettyname0 = os_release.readline()
OTP_prettyname = prettyname0.split('=')
PrettyName = ((OTP_prettyname[1]).replace('"', '')).replace('\n', '')
os_release.close()

uptime_file = open('/proc/uptime', 'r')
uptime0 = uptime_file.readline()
uptime = (uptime0.split(' '))[0]
uptime_file.close()

CPU_File = open('/proc/cpuinfo', 'r')
CPU0 = CPU_File.readlines()
CPU_Model_Name = ((((CPU0[4].split(':'))[1]).replace('\n', '')).split(' ', 1))[1]
CPU_File.close()

mem = psutil.virtual_memory()
print(os.getlogin() + '@' + os.uname().nodename)
print('OS:', '\t', '\t', PrettyName, os.uname().machine)
print('CPU:', '\t', '\t', CPU_Model_Name)
print('CPU Cores:', '\t',os.cpu_count())
print('Kernel:', '\t', os.uname().release)
print('Memory:', '\t', round((int(mem.active) / 1.074e+9),2), 'GB', '/', round((int(mem.total) / 1.074e+9),2), 'GB')
print('Uptime:', '\t', round(((float(uptime) / 60)),2), 'Minutes')
print(f'Desktop Environment:', os.environ.get("XDG_CURRENT_DESKTOP"))
