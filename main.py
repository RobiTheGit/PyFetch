#!/usr/bin/python3
import sys
import os
import psutil
import colors
print(colors.white)
OS_Release = ((open('/etc/os-release', 'r').readline().split('=')[1]).replace('"', '')).replace('\n', '')

uptime = (open('/proc/uptime', 'r').readline().split(' '))[0]
CPU_Model_Name = ((((open('/proc/cpuinfo', 'r').readlines()[4].split(':'))[1]).replace('\n', '')).split(' ', 1))[1]

mem = psutil.virtual_memory()
print(os.getlogin() + '@' + os.uname().nodename, colors.white)
print(colors.red, 'OS:', '\t', '\t', colors.white, OS_Release, os.uname().machine, colors.white)
print(colors.red, f'Shell:','\t', colors.white, str(os.environ.get("SHELL")).replace('/bin/',''), colors.white)
print(colors.red, 'CPU:', '\t', '\t', colors.white, CPU_Model_Name, colors.white)
print(colors.red, 'CPU Cores:', '\t', colors.white, os.cpu_count(), colors.white)
print(colors.red, 'Kernel:', '\t', colors.white, os.uname().release, colors.white)
print(colors.red, 'Memory:', '\t', colors.white, round((int(mem.active) / 1.074e+9),2), 'GB', '/', round((int(mem.total) / 1.074e+9),2), 'GB', colors.white)
print(colors.red, 'Uptime:', '\t', colors.white, round(((float(uptime) / 60)),2), 'Minutes', colors.white)
print(colors.red, f'Desktop:', '\t',  colors.white, os.environ.get("XDG_CURRENT_DESKTOP"), colors.white)
print(colors.red, f'Display Server:', colors.white, os.environ.get("XDG_SESSION_TYPE"), colors.white)
print(colors.red, f'Cursor Theme:  ', colors.white, os.environ.get("XCURSOR_THEME"), colors.white)
print(colors.disptest)
