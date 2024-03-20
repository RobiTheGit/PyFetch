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
bcyan = f'\033[1;38;5;14m'
magenta  = f'\033[1;38;5;13m'
bblue = f'\033[1;38;5;12m'
byellow = f'\033[1;38;5;11m'
bgreen = f'\033[1;38;5;10m'
bred = f'\033[1;38;5;9m'
bgrey = f'\033[1;38;5;7m'
grey = f'\033[1;38;5;8m'
white = f'\033[1;38;5;15m'
cyan = f'\033[1;38;5;6m'
purple = f'\033[1;38;5;5m'
blue = f'\033[1;38;5;4m'
yellow = f'\033[1;38;5;3m'
green = f'\033[1;38;5;2m'
red = f'\033[1;38;5;1m'
black = f'\033[1;38;5;0m'
none = f'\033[1;00m'


whiteBG = f'\033[1;37;47m'
cyanBG = f'\033[1;36;46m'
purpleBG = f'\033[1;35;45m'
blueBG = f'\033[1;34;44m'
yellowBG = f'\033[1;33;43m'
greenBG = f'\033[1;32;42m'
redBG = f'\033[1;31;41m'
blackBG = f'\033[1;30;40m'



textcolor = red
'''
Get System Information
'''
os.system('clear')
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
vendorstr = (open('/sys/devices/virtual/dmi/id/sys_vendor','r').readline()).replace('\n','')
RAMstr = f"{none}{round((int(mem.active) / 1.074e+9),2)} GB / {round((int(mem.total) / 1.074e+9),2)} GB"
Desktopstr = os.environ.get("XDG_CURRENT_DESKTOP")
DispServStr = os.environ.get("XDG_SESSION_TYPE").title()
CurStr = os.environ.get("XCURSOR_THEME")
Res = f'{Monitor_Width}x{Monitor_Height}'
'''
Formatting all of the information into strings that can be used in the output
'''
User = f'{textcolor}{os.getlogin()}{none}@{textcolor}{os.uname().nodename}{none}'
OS = f'{textcolor}OS:\t\t{none} {OS_Release} {os.uname().machine}'
Shell =f'{textcolor}Shell:\t\t{none} {shellstr}'
Model = f'{textcolor}Model:\t\t{none} {modelstr}'
Vendor = f'{textcolor}Vendor:\t\t{none} {vendorstr} '
CPU = f'{textcolor}CPU:{none} \t\t{none} {CPU_Model_Name} {os.cpu_count()}'
Kernel = f'{textcolor}Kernel:{none} \t{none} {os.uname().release}'
RAM = f'{textcolor}Memory:{none} \t {RAMstr} {none}'
Uptime = f'{textcolor}Uptime:{none} \t{none} {round(((float(uptime) / 60)),2)} Minutes'
Desktop = f'{textcolor}Desktop:{none} \t {none}{Desktopstr}'
DispServ = f"{textcolor}Display Server:{none}  {DispServStr}"
CursorTheme = f"{textcolor}Cursor Theme:{none}    {CurStr}"
Resolution = f"{textcolor}Resolution:{none} \t {Res}"
GPU = f"{textcolor}GPU:{none}\t\t {GPU_Pretty}"
ColoredBlocks = (f'{black}███{red}███{green}███{yellow}███{blue}███{purple}███{cyan}███{bgrey}{none}')
ColoredBlocks2 = (f'{grey}███{bred}███{bgreen}███{byellow}███{bblue}███{magenta}███{bcyan}███{white}{none}')
'''
Print system information
'''
l1  = f"        {grey}█████{none}"
l2  = f"       {grey}███████{none}"
l3  = f"       {grey}██{white}█{grey}█{white}█{grey}██{none}"
l4  = f"       {grey}█{yellow}█████{grey}█{none}"
l5  = f"     {grey}██{white}██{yellow}███{white}██{grey}██{none}"
l6  = f"    {grey}█{white}██████████{grey}██{none}"
l7  = f"   {grey}█{white}████████████{grey}██{none}"
l8  = f"   {grey}█{white}████████████{grey}███{none}"
l9  = f"  {yellow}██{grey}█{white}███████████{grey}██{yellow}█{none}"
l10 = f"{yellow}██████{grey}█{white}███████{grey}█{yellow}██████{none}"
l11 = f"{yellow}███████{grey}█{white}█████{grey}█{yellow}███████{none}"
l12 = f"  {yellow}█████{grey}███████{yellow}█████{none}"
print(f"""{none}

{l1}\t\t{User}
{l2}\t\t{none}----------------------------------
{l3}\t\t{OS}
{l4}\t\t{Shell}
{l5}\t{Model}
{l6}\t{Vendor}
{l7}\t{CPU}
{l8}\t{Kernel}
{l9}\t{RAM}
{l10}\t{Uptime}
{l11}\t{Desktop}
{l12}\t{DispServ}
\t\t\t{CursorTheme}
\t\t\t{Resolution}
\t\t\t{GPU}

\t\t\t{ColoredBlocks}
\t\t\t{ColoredBlocks2}

""")

