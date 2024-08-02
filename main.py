#!/usr/bin/python3
# Neofetch clone made for Debain based Linux, but is known to mostly work on Gentoo
# If you have a solution to use other distros, fix problems, etc, put a pull request or issue in
# PyFetch - RobiTheGit/RobiWanKenobi (2024)
# wmctrl is now required if you want the window manager stuff, but if it isn't installed, the script will still run and not cause an error

import sys, os, psutil
'''
Variable Setup
'''
Bright_Cyan = f'\033[1;38;5;14m'
Magenta  = f'\033[1;38;5;13m'
Bright_Blue = f'\033[1;38;5;12m'
Bright_Yellow = f'\033[1;38;5;11m'
Bright_Green = f'\033[1;38;5;10m'
Bright_Red = f'\033[1;38;5;9m'
Bright_Grey = f'\033[1;38;5;7m'
Grey = f'\033[1;38;5;8m'
White = f'\033[1;38;5;15m'
Cyan = f'\033[1;38;5;6m'
Purple = f'\033[1;38;5;5m'
Blue = f'\033[1;38;5;4m'
Yellow = f'\033[1;38;5;3m'
Green = f'\033[1;38;5;2m'
Red = f'\033[1;38;5;1m'
Black = f'\033[1;38;5;0m'
DefaultColor = f'\033[1;00m'


White_Background = f'\033[1;37;47m'
Cyan_Background = f'\033[1;36;46m'
Purple_Background = f'\033[1;35;45m'
Blue_Background = f'\033[1;34;44m'
Yellow_Background = f'\033[1;33;43m'
Green_Background = f'\033[1;32;42m'
Red_Background = f'\033[1;31;41m'
Black_Background = f'\033[1;30;40m'

WM = ''
c1 = White
c2 = Grey
c3 = Bright_Yellow
TextColor = c3
line_diff = 0
IconStr = ''
CurStr = ''
HideNameAndSystem = False   # I'd like to make this a command line option at some point
'''
Get System Information
'''
GPU_Pretty = ((((os.popen('lspci -nn | grep -E "Display|3D|VGA"').read()).split(':',2)[2]).split('[',2)[0]).split(' ', 1)[1] + (((os.popen('lspci -nn | grep -E "Display|3D|VGA"').read()).split(':',2)[2]).split('[',2)[1]).replace(']', '')).replace(" Corporation ",' ')
OS_Release = ((open('/etc/os-release', 'r').readline().split('=')[1]).replace('"', '')).replace('\n', '')
uptime = str(round((float((open('/proc/uptime', 'r').readline().split(' '))[0]) / 60),0)).replace('.0','')
CPU_Model_Name = ((((open('/proc/cpuinfo', 'r').readlines()[4].split(':'))[1]).replace('\n', '')).split(' ', 1))[1]
try:
    x = 0
    if os.environ.get("XDG_CURRENT_DESKTOP") == "MATE":
        x = line_diff # Change depending on how monitors.xml is set up
    Monitor_Width = ((open(f'{os.getenv("HOME")}/.config/monitors.xml', 'r').readlines()[18-x]).replace('<','').replace('>','').replace('/','').replace('\n', '').replace(' ', '').replace('width', ''))
    Monitor_Height = ((open(f'{os.getenv("HOME")}/.config/monitors.xml', 'r').readlines()[19-x]).replace('<','').replace('>','').replace('/','').replace('\n', '').replace(' ', '').replace('height', ''))

except: #This was added since monitor resolution code didn't work on Gentoo
    Monitor_Width = 'UNKNOWN'
    Monitor_Height= 'UNKNOWN'

mem = psutil.virtual_memory()
shellstr = str(os.environ.get("SHELL")).replace('/bin/','').title()
if shellstr == "Bash":
    BashVer = os.popen("bash --version | head -1 | tr ' ' '\n' | grep 'version' -A1 | grep -v 'version'").readline().replace('\n','')
    shellstr = f"Bash {BashVer}"
modelstr = (open('/sys/devices/virtual/dmi/id/product_name','r').readline()).replace('\n','')

vendorstr = (open('/sys/devices/virtual/dmi/id/sys_vendor','r').readline()).replace('\n','')
if vendorstr == "ASUSTeK COMPUTER INC.":
    vendorstr = "ASUS/ASUSTeK"

RAMstr = f"{DefaultColor}{round((int(mem.active) / 1.074e+9),2)} GB / {round((int(mem.total) / 1.074e+9),2)} GB"
Desktopstr = os.environ.get("XDG_CURRENT_DESKTOP")
if os.environ.get("XDG_SESSION_TYPE") == 'tty':
    Desktopstr = "Tty"
try:
    WM = os.popen("wmctrl -m | awk -F: '/Name: /{print $2}'").read().replace('\n', '').strip()
except:
    WM = ""
if Desktopstr == "GNOME-Flashback:GNOME:":
    Desktopstr = (os.popen('gnome-shell --version')).read().replace(' Shell ', ' Flashback ').replace('\n', '')
if Desktopstr == "X-Cinnamon":
        Desktopstr = 'Cinnamon'
if Desktopstr == "GNOME" and not Desktopstr == "GNOME-Flashback:GNOME:":
    Desktopstr = (os.popen('gnome-shell --version')).read().replace(' Shell ', ' ').replace('\n', '')
else:
    DispServStr = os.environ.get("XDG_SESSION_TYPE").title()

CurStr = os.environ.get("XCURSOR_THEME")

if CurStr == None:
    CurStr = (os.popen('gtk-query-settings gtk-cursor-theme-name')).read().replace('"', '').replace('\n', '').replace('gtk-cursor-theme-name:', '').strip()


IconStr = (os.popen('gtk-query-settings gtk-icon-theme-name')).read().replace('"', '').replace('\n', '').replace('gtk-icon-theme-name:', '').strip()

ThemeStr = (os.popen('gtk-query-settings gtk-theme-name')).read().replace('"', '').replace('\n', '').replace('gtk-theme-name:', '').strip()

Res = f'{Monitor_Width}x{Monitor_Height}'
'''
Formatting all of the information into strings that can be used in the output
'''
if HideNameAndSystem == False:
    User    = f'{TextColor}{os.getlogin()}{DefaultColor}@{TextColor}{os.uname().nodename}{DefaultColor}'    #   This is actually grabbing the username and system name, all from raw python
else:
    User    = f'{TextColor}user{DefaultColor}@{TextColor}linux{DefaultColor}'   #   This Code just prevents the actual username of the system, and the system name from being shown. This is used mostly for the readme

OS             = f'{TextColor}OS:\t\t{DefaultColor} {OS_Release} {os.uname().machine}'
Shell          = f'{TextColor}Terminal Shell:\t{DefaultColor} {shellstr}'
Model          = f'{TextColor}Model:\t\t{DefaultColor} {modelstr}'
Vendor         = f'{TextColor}Vendor:\t\t{DefaultColor} {vendorstr} '
CPU            = f'{TextColor}CPU:{DefaultColor} \t\t{DefaultColor} {CPU_Model_Name}({os.cpu_count()})'
Kernel         = f'{TextColor}Kernel:{DefaultColor} \t{DefaultColor} {os.uname().release}'
RAM            = f'{TextColor}Memory (RAM):{DefaultColor} \t {RAMstr} {DefaultColor}'
Uptime         = f'{TextColor}Uptime:{DefaultColor} \t{DefaultColor} {uptime} Minutes'
Desktop        = f'{TextColor}Desktop:{DefaultColor} \t {DefaultColor}{Desktopstr}'
DispServ       = f"{TextColor}Display Server:{DefaultColor}  {DispServStr}"
CursorTheme    = f"{TextColor}Cursor Theme:{DefaultColor}    {CurStr}"
if ThemeStr != '':
    GTKTheme       = f"{TextColor}GTK Theme:{DefaultColor}       {ThemeStr}"

if IconStr != '':
    IconTheme      = f"{TextColor}Icon Theme:{DefaultColor}      {IconStr}"

Resolution     = f"{TextColor}Resolution:{DefaultColor} \t {Res}"
GPU            = f"{TextColor}GPU:{DefaultColor}\t\t {GPU_Pretty}"
if WM == "":
    WM_Pretty  = ""
else:
    WM_Pretty  = f"{TextColor}Window Manager:{DefaultColor}\t {WM}"
Arch           = f"{TextColor}CPU Type:{DefaultColor}\t {(os.popen('arch')).read()}"
ColoredBlocks  = (f'{Black}███{Red}███{Green}███{Yellow}███{Blue}███{Purple}███{Cyan}███{Bright_Grey}███{DefaultColor}')
ClrBlk_Lighter = (f'{Grey}███{Bright_Red}███{Bright_Green}███{Bright_Yellow}███{Bright_Blue}███{Magenta}███{Bright_Cyan}███{White}███{DefaultColor}')
'''
Print system information

Image res, 21c x 12c; c = characters
'''
l1  = f"        {c2}█████{DefaultColor}        "
l2  = f"       {c2}███████{DefaultColor}       "
l3  = f"       {c2}██{c1}█{c2}█{c1}█{c2}██{DefaultColor}       "
l4  = f"       {c2}█{c3}█████{c2}█{DefaultColor}       "
l5  = f"     {c2}██{c1}██{c3}███{c1}██{c2}██{DefaultColor}     "
l6  = f"    {c2}█{c1}██████████{c2}██{DefaultColor}    "
l7  = f"   {c2}█{c1}████████████{c2}██{DefaultColor}   "
l8  = f"   {c2}█{c1}████████████{c2}███{DefaultColor}  "
l9  = f"  {c3}██{c2}█{c1}███████████{c2}██{c3}█{DefaultColor}  "
l10 = f"{c3}██████{c2}█{c1}███████{c2}█{c3}██████{DefaultColor}"
l11 = f"{c3}███████{c2}█{c1}█████{c2}█{c3}███████{DefaultColor}"
l12 = f"  {c3}█████{c2}███████{c3}█████{DefaultColor}  "


print(f"{DefaultColor}\n                        {User}")
print(f"                        ----------------------------------")
print(f"{l1}\t{OS}")
print(f"{l2}\t{Shell}")
print(f"{l3}\t{Model}")
print(f"{l4}\t{Vendor}")
print(f"{l5}\t{CPU}")
print(f"{l6}\t{Kernel}")
print(f"{l7}\t{RAM}")
print(f"{l8}\t{Uptime}")
print(f"{l9}\t{Desktop}")
print(f"{l10}\t{DispServ}")
if WM_Pretty != "":
    print(f"{l11}\t{WM_Pretty}")
    print(f"{l12}\t{Resolution}")
    print(f"                        {GPU}")
else:
    print(f"{l11}\t{Resolution}")
    print(f"{l12}\t{GPU}")
if os.environ.get("XDG_SESSION_TYPE") == 'tty':
    pass
else:
    print(f"                        {CursorTheme}")
    if IconStr != '':
        print(f"                        {IconTheme}")
    if ThemeStr != '':
        print(f"                        {GTKTheme}")


   # print(f"                        {CursorTheme}")

print(f"                        {Arch}")
print(f"\n                        {ColoredBlocks}")
print(f"                        {ClrBlk_Lighter}")

