#!/usr/bin/python3
# Made for Debain based Linux
# If you have a solution to use other distors, fix problems, etc, put a pull request or issue in
# PyFetch - RobiTheGit (2024)
import sys
import os
import psutil
import colors
gpu1 = (((os.popen('lspci -nn | grep -E "Display|3D|VGA"').read()).split(':',2)[2]).split('[',2)[0]).split(' ', 1)[1]
gpu2 = (((os.popen('lspci -nn | grep -E "Display|3D|VGA"').read()).split(':',2)[2]).split('[',2)[1]).replace(']', '')
GPU_Pretty = gpu1 + gpu2
print(colors.white)
OS_Release = ((open('/etc/os-release', 'r').readline().split('=')[1]).replace('"', '')).replace('\n', '')
uptime = (open('/proc/uptime', 'r').readline().split(' '))[0]
CPU_Model_Name = ((((open('/proc/cpuinfo', 'r').readlines()[4].split(':'))[1]).replace('\n', '')).split(' ', 1))[1]
Monitor_Width = ((open(f'{os.getenv("HOME")}/.config/monitors.xml', 'r').readlines()[18]).replace('<','').replace('>','').replace('/','').replace('\n', '').replace(' ', '').replace('width', ''))
Monitor_Height = ((open(f'{os.getenv("HOME")}/.config/monitors.xml', 'r').readlines()[19]).replace('<','').replace('>','').replace('/','').replace('\n', '').replace(' ', '').replace('height', ''))
mem = psutil.virtual_memory()
print(colors.red, os.getlogin() + colors.white + '@' + colors.red +os.uname().nodename, colors.white)
print(colors.red, 'OS:', '\t', '\t', colors.white, OS_Release, os.uname().machine, colors.white)
print(colors.red, f'Shell:','\t', colors.white, str(os.environ.get("SHELL")).replace('/bin/','').title(), colors.white)
print(colors.red, 'CPU:', '\t', '\t', colors.white, CPU_Model_Name, f'({os.cpu_count()})', colors.white)
print(colors.red, 'Kernel:', '\t', colors.white, os.uname().release, colors.white)
print(colors.red, 'Memory:', '\t', colors.white, round((int(mem.active) / 1.074e+9),2), 'GB', '/', round((int(mem.total) / 1.074e+9),2), 'GB', colors.white)
print(colors.red, 'Uptime:', '\t', colors.white, round(((float(uptime) / 60)),2), 'Minutes', colors.white)
print(colors.red, f'Desktop:', '\t',  colors.white, os.environ.get("XDG_CURRENT_DESKTOP"), colors.white)
print(colors.red, f'Display Server:', colors.white, os.environ.get("XDG_SESSION_TYPE").title(), colors.white)
print(colors.red, f'Cursor Theme:  ', colors.white, os.environ.get("XCURSOR_THEME"), colors.white)
print(colors.red, f'Resolution:', '\t',colors.white,f'{Monitor_Width}x{Monitor_Height}' , colors.white)
print(colors.red, f'GPU:'+ '\t'+ '\t',colors.white, GPU_Pretty, colors.white)

print(colors.disptest)
