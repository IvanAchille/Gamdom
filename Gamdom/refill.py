import os
import time
import random
import click
from colorama import init
from colors import red, green, blue, white, black, yellow
init()
os.system("cls")
db_rol_name = "rlcs.coins" #Get file name
refillcoins = open(db_rol_name, 'w+')
print(yellow(" ============ Gamdom REFILL System (GRS) ============"))
print("")
print(green("Gamdom Refill Options:", style="bold"))
print(yellow("""
1) $5 USD (5000 Coins)
2) $10 USD (10000 Coins)
3) $20 USD (20000 Coins)
 """, style="bold"))
wr = str(input(green("GRS: ")))
while True:
	if wr=="1":
		refillcoins.write("5000")
		rf = "$5 USD"
		break
	elif wr=="2":
		refillcoins.write("10000")
		rf = "$10 USD"
		break
	elif wr=="3":
		refillcoins.write("20000")
		rf = "$20 USD"
		break
	else:
		print(red("ERROR: Wrong Option",style="bold"))
	wr = str(input(green("GRS: ")))
print("")
grsmsg = yellow("GRS: ",style="bold")
os.system("cls")
print(green(str("""
_____                     _
|  __ \                   | |
| |  \/ __ _ _ __ ___   __| | ___  _ __ ___
| | __ / _` | '_ ` _ \ / _` |/ _ \| '_ ` _ ``
| |_\ \ (_| | | | | | | (_| | (_) | | | | | |
 \____/\__,_|_| |_| |_|\__,_|\___/|_| |_| |_|

     ~~~ Developed by Ivan Achille ~~~

"""), style='bold'))


print(grsmsg+green("Refilling "+rf+"..."))
time.sleep(2)
print(grsmsg+green("♠ Refill Complete ♠"))
