#!/usr/bin/python3
# Made for Debain based Linux
# If you have a solution to use other distros, fix problems, etc, put a pull request or issue in
# PyFetch - RobiTheGit (2024)
import sys
import os
import psutil
'''
Variable Setup
'''
white = f'\033[1;37m'
cyan = f'\033[1;36m'
magenta = f'\033[1;35m'
blue = f'\033[1;34m'
yellow = f'\033[1;33m'
green = f'\033[1;32m'
red = f'\033[1;31m'
none = f'\033[1;00m'

gpu1 = (((os.popen('lspci -nn | grep -E "Display|3D|VGA"').read()).split(':',2)[2]).split('[',2)[0]).split(' ', 1)[1]
gpu2 = (((os.popen('lspci -nn | grep -E "Display|3D|VGA"').read()).split(':',2)[2]).split('[',2)[1]).replace(']', '')
GPU_Pretty = gpu1 + gpu2
OS_Release = ((open('/etc/os-release', 'r').readline().split('=')[1]).replace('"', '')).replace('\n', '')
uptime = (open('/proc/uptime', 'r').readline().split(' '))[0]
CPU_Model_Name = ((((open('/proc/cpuinfo', 'r').readlines()[4].split(':'))[1]).replace('\n', '')).split(' ', 1))[1]
Monitor_Width = ((open(f'{os.getenv("HOME")}/.config/monitors.xml', 'r').readlines()[18]).replace('<','').replace('>','').replace('/','').replace('\n', '').replace(' ', '').replace('width', ''))
Monitor_Height = ((open(f'{os.getenv("HOME")}/.config/monitors.xml', 'r').readlines()[19]).replace('<','').replace('>','').replace('/','').replace('\n', '').replace(' ', '').replace('height', ''))
mem = psutil.virtual_memory()
shellstr = str(os.environ.get("SHELL")).replace('/bin/','').title()
modelstr = (open('/sys/devices/virtual/dmi/id/product_name','r').readline()).replace('\n','')
User = f'{red} {os.getlogin()}{none}@{red}{os.uname().nodename}{none}'
vendorstr = (open('/sys/devices/virtual/dmi/id/sys_vendor','r').readline()).replace('\n','')
RAMstr = f"{none}{round((int(mem.active) / 1.074e+9),2)} GB / {round((int(mem.total) / 1.074e+9),2)} GB"
Desktopstr = os.environ.get("XDG_CURRENT_DESKTOP")
DispServStr = os.environ.get("XDG_SESSION_TYPE").title()
CurStr = os.environ.get("XCURSOR_THEME")

OS = f'{red} OS:\t\t{none} {OS_Release} {os.uname().machine}'
Shell =f'{red} Shell:\t\t{none} {shellstr}'
Model = f'{red} Model:\t\t{none} {modelstr}'
Vendor = f'{red} Vendor:\t{none} {vendorstr} '
CPU = f'{red} CPU: \t\t{none} {CPU_Model_Name} {os.cpu_count()}'
Kernel = f'{red} Kernel: \t{none} {os.uname().release}'
RAM = f'{red} Memory: \t {RAMstr} {none}'
Uptime = f'{red} Uptime: \t{none} {round(((float(uptime) / 60)),2)} Minutes'
Desktop = f'{red} Desktop: \t {none}{Desktopstr}'
DispServ = f"{red} Display Server:{none} {DispServStr}"
CursorTheme = f"{red} Cursor Theme:  {none} {CurStr}"
Resolution = f"{red} Resolution: \t{none} {Monitor_Width}x{Monitor_Height}"
GPU = f"{red} GPU:\t\t {none}{GPU_Pretty}"
ColoredBlocks = ('\n\033[0;31;31m████\033[0;32;32m████\033[0;33;33m████\033[0;34;34m████\033[0;35;35m████\033[0;36;36m████\033[0;37;37m████\n\033[0;31;31m████\033[0;32;32m████\033[0;33;33m████\033[0;34;34m████\033[0;35;35m████\033[0;36;36m████\033[0;37;37m████\n')

print(f"""{none}
{User}
{OS}
{Shell}
{Model}
{Vendor}
{CPU}
{Kernel}
{RAM}
{Uptime}
{Desktop}
{DispServ}
{CursorTheme}
{Resolution}
{GPU}
{ColoredBlocks}
      """)
