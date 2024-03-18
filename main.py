#!/usr/bin/python3
# Made for Debain based Linux
# If you have a solution to use other distros, fix problems, etc, put a pull request or issue in
# PyFetch - RobiTheGit (2024)
import sys
import os
import psutil
import colors
'''
Variable Setup
'''
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
User = f'{colors.red} {os.getlogin()}{colors.none}@{colors.red}{os.uname().nodename}{colors.none}'
vendorstr = (open('/sys/devices/virtual/dmi/id/sys_vendor','r').readline()).replace('\n','')
RAMstr = f"{colors.none}{round((int(mem.active) / 1.074e+9),2)} GB / {round((int(mem.total) / 1.074e+9),2)} GB"
Desktopstr = os.environ.get("XDG_CURRENT_DESKTOP")
DispServStr = os.environ.get("XDG_SESSION_TYPE").title()
CurStr = os.environ.get("XCURSOR_THEME")

OS = f'{colors.red} OS:\t\t{colors.none} {OS_Release} {os.uname().machine}'
Shell =f'{colors.red} Shell:\t\t{colors.none} {shellstr}'
Model = f'{colors.red} Model:\t\t{colors.none} {modelstr}'
Vendor = f'{colors.red} Vendor:\t{colors.none} {vendorstr} '
CPU = f'{colors.red} CPU: \t\t{colors.none} {CPU_Model_Name} {os.cpu_count()}'
Kernel = f'{colors.red} Kernel: \t{colors.none} {os.uname().release}'
RAM = f'{colors.red} Memory: \t {RAMstr} {colors.none}'
Uptime = f'{colors.red} Uptime: \t{colors.none} {round(((float(uptime) / 60)),2)} Minutes'
Desktop = f'{colors.red} Desktop: \t {colors.none}{Desktopstr}'
DispServ = f"{colors.red} Display Server:{colors.none} {DispServStr}"
CursorTheme = f"{colors.red} Cursor Theme:  {colors.none} {CurStr}"
Resolution = f"{colors.red} Resolution: \t{colors.none} {Monitor_Width}x{Monitor_Height}"
GPU = f"{colors.red} GPU:\t\t {colors.none}{GPU_Pretty}"
ColoredBlocks = (f'\n{colors.disptest}\n{colors.disptest}\n')

print(f"""{colors.none}
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
