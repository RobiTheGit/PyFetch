#!/usr/bin/python3
# Neofetch clone made for Debain based Linux, but is known to mostly work on Gentoo
#
# If you have a solution to use other distros, fix problems, etc, put a pull request or issue in
#
# PyFetch - RobiTheGit/RobiWanKenobi (2024)
#
# wmctrl is now required if you want the window manager stuff, but if it isn't installed, the script will still run and not cause an error
#
# For ASCII Images, keep them 22 Characters by 12 Characters

import os, psutil
from sys import argv
try:
    script, flgs = argv
except:
    flgs = ''

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
img = ''
line_diff = 0
IconStr = ''
CurStr = ''
ThemeStr = ''
if '-h' in flgs:
    HideNameAndSystem = True
else:
    HideNameAndSystem = False
'''
Distro
'''
OS_Release = ((open('/etc/os-release', 'r').readline().split('=')[1]).replace('"', '')).replace('\n', '')
try:
    if OS_Release.startswith("Debian"):
        img = 'deb'
    elif OS_Release.startswith("Arch"):
        img = 'arch'
    else:
        img = 'generic'
except:
    img = 'test'
'''
Image res, 26c x 12c; c = characters
'''


if img == 'generic': #  Tux
    c1 = White
    c2 = Grey
    c3 = Bright_Yellow
elif img == 'deb':
    c1 = Red
    c2 = c1
    c3 = Bright_Red
elif img == 'arch':
    c1 = Cyan
    c2 = Blue
    c3 = Cyan
else:
    c1 = White
    c2 = c1
    c3 = c1

TextColor = c3
'''
Tux Penguin Image
'''
tux_l1  = f"        {c2}█████{DefaultColor}            "
tux_l2  = f"       {c2}███████{DefaultColor}           "
tux_l3  = f"       {c2}██{c1}█{c2}█{c1}█{c2}██{DefaultColor}           "
tux_l4  = f"       {c2}█{c3}█████{c2}█{DefaultColor}           "
tux_l5  = f"     {c2}██{c1}██{c3}███{c1}██{c2}██{DefaultColor}         "
tux_l6  = f"    {c2}█{c1}██████████{c2}██{DefaultColor}        "
tux_l7  = f"   {c2}█{c1}████████████{c2}██{DefaultColor}       "
tux_l8  = f"   {c2}█{c1}████████████{c2}███{DefaultColor}      "
tux_l9  = f"  {c3}██{c2}█{c1}███████████{c2}██{c3}█{DefaultColor}      "
tux_l10 = f"{c3}██████{c2}█{c1}███████{c2}█{c3}██████{DefaultColor}    "
tux_l11 = f"{c3}███████{c2}█{c1}█████{c2}█{c3}███████{DefaultColor}    "
tux_l12 = f"  {c3}█████{c2}███████{c3}█████{DefaultColor}      "

'''
TEST IMAGE
'''
t1  = f'{c1}                          {DefaultColor}'
t2  = f'{c2}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ {DefaultColor}'
t3  = f'{c3}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ {DefaultColor}'
t4  = f'{c1}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ {DefaultColor}'
t5  = f'{c2}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ {DefaultColor}'
t6  = f'{c3}░░░░░░░░░░░░░░░░░░░░░░░░░ {DefaultColor}'
t7  = f'{c1}░░░░░░░░░░░░░░░░░░░░░░░░░ {DefaultColor}'
t8  = f'{c2}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ {DefaultColor}'
t9  = f'{c3}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ {DefaultColor}'
t10 = f'{c1}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ {DefaultColor}'
t11 = f'{c2}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ {DefaultColor}'
t12 = f'{c3}                          {DefaultColor}'

'''
Debian Image
'''
deb1  = f"      {c1}_,###._{DefaultColor}       "
deb2  = f"    {c1},#########.{DefaultColor}     "
deb3  = f"  {c1}.######^######.{DefaultColor}   "
deb4  = f"{c1}.####'     `####{DefaultColor}    "
deb5  = f" {c1}####' ,###. `###:{DefaultColor}  "
deb6  = f" {c1}###'  ##'`# ,###{DefaultColor}   "
deb7  = f" {c1}###.  ###._,###'{DefaultColor}   "
deb8  = f" {c1}`###  `######'{DefaultColor}     "
deb9  = f"  {c1}`###    `''{DefaultColor}       "
deb10 = f"   {c1}`###.{DefaultColor}            "
deb11 = f"     {c1}`###,{DefaultColor}          "
deb12 = f"       {c1}`'##:.{DefaultColor}       "

'''
the "i use arch btw" image
'''
AB1   =  '                '
arch1 = f'      {c1}/\\\{DefaultColor}       '
arch2 = f'     {c1}/  \\\{DefaultColor}      '
arch3 = f'    {c1}/\\\   \\\{DefaultColor}    '
arch4 = f'   {c1}/      \\\{DefaultColor}    '
arch5 = f'  {c2}/   ,,   \\\{DefaultColor}   '
arch6 = f' {c2}/   |  |  -\\\{DefaultColor}  '
arch7 = f"{c2}/_-''    ''-_\\\{DefaultColor} "


# Format:
# Line length -1 (for whitespace setting)
# Line 1
# ...  (the other lines)
# Line 12
blank = ' '
IMGS = {
    'test': [26, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12],
    'generic': [25, tux_l1, tux_l2, tux_l3, tux_l4, tux_l5, tux_l6, tux_l7, tux_l8, tux_l9, tux_l10, tux_l11, tux_l12],
    'deb': [20, deb1, deb2, deb3, deb4, deb5, deb6, deb7, deb8, deb9, deb10, deb11, deb12],
    'arch': [16, arch1, arch2, arch3, arch4, arch5, arch6, arch7, AB1, AB1, AB1, AB1, AB1]
    }

'''
Get System Information
'''

'''
GPU & CPU
'''
GPU_Pretty = ((((os.popen('lspci -nn | grep -E "Display|3D|VGA"').read()).split(':',2)[2]).split('[',2)[0]).split(' ', 1)[1] + (((os.popen('lspci -nn | grep -E "Display|3D|VGA"').read()).split(':',2)[2]).split('[',2)[1]).replace(']', '')).replace(" Corporation ",' ')

CPU_Model_Name = ((((open('/proc/cpuinfo', 'r').readlines()[4].split(':'))[1]).replace('\n', '')).split(' ', 1))[1]

'''
Uptime
'''
uptime = str(round((float((open('/proc/uptime', 'r').readline().split(' '))[0]) / 60),0)).replace('.0','')

'''
Monitor
'''
try:

    # Change line_diff depending on how monitors.xml is set up
    Monitor_Width = ((open(f'{os.getenv("HOME")}/.config/monitors.xml', 'r').readlines()[18-line_diff]).replace('<','').replace('>','').replace('/','').replace('\n', '').replace(' ', '').replace('width', ''))
    Monitor_Height = ((open(f'{os.getenv("HOME")}/.config/monitors.xml', 'r').readlines()[19-line_diff]).replace('<','').replace('>','').replace('/','').replace('\n', '').replace(' ', '').replace('height', ''))

except: #This was added since monitor resolution code didn't work on Gentoo
    Monitor_Width = 'UNKNOWN'
    Monitor_Height= 'UNKNOWN'

Res = f'{Monitor_Width}x{Monitor_Height}'

'''
RAM & Shell
'''

mem = psutil.virtual_memory()
RAMstr = f"{DefaultColor}{round((int(mem.active) / 1.074e+9),2)} GB / {round((int(mem.total) / 1.074e+9),2)} GB"

shellstr = str(os.environ.get("SHELL")).replace('/bin/','').title()
if shellstr == "Bash":
    BashVer = os.popen("bash --version | head -1 | tr ' ' '\n' | grep 'version' -A1 | grep -v 'version'").readline().replace('\n','')
    shellstr = f"Bash {BashVer}"

'''
Hardware
'''

modelstr = (open('/sys/devices/virtual/dmi/id/product_name','r').readline()).replace('\n','')

vendorstr = (open('/sys/devices/virtual/dmi/id/sys_vendor','r').readline()).replace('\n','')
if vendorstr == "ASUSTeK COMPUTER INC.":
    vendorstr = "ASUS/ASUSTeK"

'''
Desktop, Windowing System, & Window Manager
'''

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

'''
Themes
'''
CurStr = os.environ.get("XCURSOR_THEME")

if CurStr == None:
    CurStr = (os.popen('gtk-query-settings gtk-cursor-theme-name')).read().replace('"', '').replace('\n', '').replace('gtk-cursor-theme-name:', '').strip()


IconStr = (os.popen('gtk-query-settings gtk-icon-theme-name')).read().replace('"', '').replace('\n', '').replace('gtk-icon-theme-name:', '').strip()

ThemeStr = (os.popen('gtk-query-settings gtk-theme-name')).read().replace('"', '').replace('\n', '').replace('gtk-theme-name:', '').strip()

'''
Formatting all of the information into strings that can be used in the output
'''
if HideNameAndSystem == False:
    User    = f'{TextColor}{os.getlogin()}{DefaultColor}@{TextColor}{os.uname().nodename}{DefaultColor}'    #   This is actually grabbing the username and system name, all from raw python
else:
    User    = f'{TextColor}user{DefaultColor}@{TextColor}linux{DefaultColor}'   #   This just puts a placeholder user and system name in, this is what I use in the screenshots

OS             = f'{TextColor}OS:{DefaultColor} {OS_Release} {os.uname().machine}'
Shell          = f'{TextColor}Terminal Shell: {DefaultColor}{shellstr}'
Model          = f'{TextColor}Model: {DefaultColor}{modelstr}'
Vendor         = f'{TextColor}Vendor: {DefaultColor}{vendorstr} '
CPU            = f'{TextColor}CPU: {DefaultColor}{DefaultColor}{CPU_Model_Name}({os.cpu_count()})'
Kernel         = f'{TextColor}Kernel: {DefaultColor}{DefaultColor}{os.uname().release}'
RAM            = f'{TextColor}Memory (RAM): {DefaultColor}{RAMstr}{DefaultColor}'
Uptime         = f'{TextColor}Uptime: {DefaultColor}{DefaultColor}{uptime} Minutes'
Desktop        = f'{TextColor}Desktop: {DefaultColor}{DefaultColor}{Desktopstr}'
DispServ       = f"{TextColor}Display Server: {DefaultColor}{DispServStr}"
CursorTheme    = f"{TextColor}Cursor Theme: {DefaultColor}{CurStr}"
if ThemeStr != '':
    GTKTheme       = f"{TextColor}GTK Theme: {DefaultColor}{ThemeStr}"

if IconStr != '':
    IconTheme      = f"{TextColor}Icon Theme: {DefaultColor}{IconStr}"

Resolution     = f"{TextColor}Resolution: {DefaultColor}{Res}"
GPU            = f"{TextColor}GPU: {DefaultColor}{GPU_Pretty}"
if WM == "":
    WM_Pretty  = ""
else:
    WM_Pretty  = f"{TextColor}Window Manager: {DefaultColor}{WM}"
Arch           = f"{TextColor}CPU Type: {DefaultColor}{(os.popen('arch')).read()}"
ColoredBlocks  = (f'{Black}███{Red}███{Green}███{Yellow}███{Blue}███{Purple}███{Cyan}███{Bright_Grey}███{DefaultColor}')
ClrBlk_Lighter = (f'{Grey}███{Bright_Red}███{Bright_Green}███{Bright_Yellow}███{Bright_Blue}███{Magenta}███{Bright_Cyan}███{White}███{DefaultColor}')
'''
Print system information
'''

blank *= IMGS[img][0]

print(f"{DefaultColor}\n{blank}{User}")
print(f"{blank}----------------------------------")
print(f"{IMGS[img][1]}{OS}")
print(f"{IMGS[img][2]}{Shell}")
print(f"{IMGS[img][3]}{Model}")
print(f"{IMGS[img][4]}{Vendor}")
print(f"{IMGS[img][5]}{CPU}")
print(f"{IMGS[img][6]}{Kernel}")
print(f"{IMGS[img][7]}{RAM}")
print(f"{IMGS[img][8]}{Uptime}")
print(f"{IMGS[img][9]}{Desktop}")
print(f"{IMGS[img][10]}{DispServ}")
if WM_Pretty != "":
    print(f"{IMGS[img][11]}{WM_Pretty}")
    print(f"{IMGS[img][12]}{Resolution}")
    print(f"{blank}{GPU}")
else:
    print(f"{IMGS[img][11]}{Resolution}")
    print(f"{IMGS[img][12]}{GPU}")
if os.environ.get("XDG_SESSION_TYPE") == 'tty':
    pass
else:
    print(f"{blank}{CursorTheme}")
    if IconStr != '':
        print(f"{blank}{IconTheme}")
    if ThemeStr != '':
        print(f"{blank}{GTKTheme}")

print(f"{blank}{Arch}")
print(f"\n{blank}{ColoredBlocks}")
print(f"{blank}{ClrBlk_Lighter}")

