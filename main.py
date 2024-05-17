#!/usr/bin/python3
# Made for Debain based Linux
# If you have a solution to use other distros, fix problems, etc, put a pull request or issue in
# PyFetch - RobiTheGit/RobiWanKenobi (2024)
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


c1 = white
c2 = grey
c3 = yellow
textcolor = c3
HideNameAndSystem = False
'''
Get System Information
'''
gpu1 = (((os.popen('lspci -nn | grep -E "Display|3D|VGA"').read()).split(':',2)[2]).split('[',2)[0]).split(' ', 1)[1]
gpu2 = (((os.popen('lspci -nn | grep -E "Display|3D|VGA"').read()).split(':',2)[2]).split('[',2)[1]).replace(']', '')
GPU_Pretty = gpu1 + gpu2
OS_Release = ((open('/etc/os-release', 'r').readline().split('=')[1]).replace('"', '')).replace('\n', '')
uptime = (open('/proc/uptime', 'r').readline().split(' '))[0]
CPU_Model_Name = ((((open('/proc/cpuinfo', 'r').readlines()[4].split(':'))[1]).replace('\n', '')).split(' ', 1))[1]
try:
    x = 0
    if os.environ.get("XDG_CURRENT_DESKTOP") == "MATE":
        x = 0 # Change depending on how monitors.xml is set up
    Monitor_Width = ((open(f'{os.getenv("HOME")}/.config/monitors.xml', 'r').readlines()[18-x]).replace('<','').replace('>','').replace('/','').replace('\n', '').replace(' ', '').replace('width', ''))
    Monitor_Height = ((open(f'{os.getenv("HOME")}/.config/monitors.xml', 'r').readlines()[19-x]).replace('<','').replace('>','').replace('/','').replace('\n', '').replace(' ', '').replace('height', ''))

except: #This was added since monitor resolution code didn't work on Gentoo, nor does it work in MATE
    Monitor_Width = 'UNKNOWN'
    Monitor_Height= 'UNKNOWN'

mem = psutil.virtual_memory()
shellstr = str(os.environ.get("SHELL")).replace('/bin/','').title()
modelstr = (open('/sys/devices/virtual/dmi/id/product_name','r').readline()).replace('\n','')

vendorstr = (open('/sys/devices/virtual/dmi/id/sys_vendor','r').readline()).replace('\n','')
if vendorstr == "ASUSTeK COMPUTER INC.":
    vendorstr = "ASUS"

RAMstr = f"{none}{round((int(mem.active) / 1.074e+9),2)} GB / {round((int(mem.total) / 1.074e+9),2)} GB"
Desktopstr = os.environ.get("XDG_CURRENT_DESKTOP")
if Desktopstr == "GNOME-Flashback:GNOME:":
    Desktopstr = (os.popen('gnome-shell --version')).read().replace(' Shell ', ' Flashback ').replace('\n', '')

if Desktopstr == "GNOME" and not Desktopstr == "GNOME-Flashback:GNOME:":
    Desktopstr = (os.popen('gnome-shell --version')).read().replace(' Shell ', ' ').replace('\n', '')
    if Desktopstr.startswith("GNOME 4") or Desktopstr.startswith("GNOME 3"):
        WM = "Mutter"
    else:
        WM = "Metacity"

if os.environ.get("XDG_CURRENT_DESKTOP") == "KDE":
    WM = "KWin"
if os.environ.get("XDG_CURRENT_DESKTOP") == "LXDE":
    WM = "LXDM"
if os.environ.get("XDG_CURRENT_DESKTOP") == "GNOME-Flashback:GNOME:" or os.environ.get("XDG_CURRENT_DESKTOP") == "MATE":
    WM = "Metacity"
else:
    DispServStr = os.environ.get("XDG_SESSION_TYPE").title()
CurStr = os.environ.get("XCURSOR_THEME")
Res = f'{Monitor_Width}x{Monitor_Height}'
'''
Formatting all of the information into strings that can be used in the output
'''
if HideNameAndSystem == False:
    User    = f'{textcolor}{os.getlogin()}{none}@{textcolor}{os.uname().nodename}{none}'    #   This is actually grabbing the username and system name, all from raw python
else:
    User    = f'{textcolor}user{none}@{textcolor}linux{none}'   #   This Code just prevents the actual username of the system, and the system name from being shown.

OS          = f'{textcolor}OS:\t\t{none} {OS_Release} {os.uname().machine}'
Shell       = f'{textcolor}Terminal Shell:\t{none} {shellstr}'
Model       = f'{textcolor}Model:\t\t{none} {modelstr}'
Vendor      = f'{textcolor}Vendor:\t\t{none} {vendorstr} '
CPU         = f'{textcolor}CPU:{none} \t\t{none} {CPU_Model_Name}({os.cpu_count()})'
Kernel      = f'{textcolor}Kernel:{none} \t{none} {os.uname().release}'
RAM         = f'{textcolor}Memory:{none} \t {RAMstr} {none}'
Uptime      = f'{textcolor}Uptime:{none} \t{none} {round(((float(uptime) / 60)),2)} Minutes'
Desktop     = f'{textcolor}Desktop:{none} \t {none}{Desktopstr}'
DispServ    = f"{textcolor}Display Server:{none}  {DispServStr}"
CursorTheme = f"{textcolor}Cursor Theme:{none}    {CurStr}"
Resolution  = f"{textcolor}Resolution:{none} \t {Res}"
GPU         = f"{textcolor}GPU:{none}\t\t {GPU_Pretty}"
WM_Pretty   = f"{textcolor}Window Manager:{none}\t {WM}"
ColoredBlocks = (f'{black}███{red}███{green}███{yellow}███{blue}███{purple}███{cyan}███{bgrey}███{none}')
ColoredBlocks_Lighter = (f'{grey}███{bred}███{bgreen}███{byellow}███{bblue}███{magenta}███{bcyan}███{white}███{none}')
'''
Print system information
'''
l1  = f"        {c2}█████{none}"
l2  = f"       {c2}███████{none}"
l3  = f"       {c2}██{c1}█{c2}█{c1}█{c2}██{none}"
l4  = f"       {c2}█{c3}█████{c2}█{none}"
l5  = f"     {c2}██{c1}██{c3}███{c1}██{c2}██{none}"
l6  = f"    {c2}█{c1}██████████{c2}██{none}"
l7  = f"   {c2}█{c1}████████████{c2}██{none}"
l8  = f"   {c2}█{c1}████████████{c2}███{none}"
l9  = f"  {c3}██{c2}█{c1}███████████{c2}██{c3}█{none}"
l10 = f"{c3}██████{c2}█{c1}███████{c2}█{c3}██████{none}"
l11 = f"{c3}███████{c2}█{c1}█████{c2}█{c3}███████{none}"
l12 = f"  {c3}█████{c2}███████{c3}█████{none}"
print(f"""{none}
{l1}\t\t\t{User}
{l2}\t\t\t----------------------------------
{l3}\t\t\t{OS}
{l4}\t\t\t{Shell}
{l5}\t\t{Model}
{l6}\t\t{Vendor}
{l7}\t\t{CPU}
{l8}\t\t{Kernel}
{l9}\t\t{RAM}
{l10}\t\t{Uptime}
{l11}\t\t{Desktop}
{l12}\t\t{DispServ}
\t\t\t\t{CursorTheme}
\t\t\t\t{Resolution}
\t\t\t\t{GPU}
\t\t\t\t{WM_Pretty}

\t\t\t\t{ColoredBlocks}
\t\t\t\t{ColoredBlocks_Lighter}

""")

