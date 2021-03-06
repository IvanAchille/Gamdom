

#_-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-_

# SCRIPT DEVELOPED BY Ivan Achille

#_-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-__-_-_

def game():

	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ IMPORT PACKAGES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	import os
	import time
	import random
	from colorama import init
	from colors import red, green, blue, white, black, yellow
	init()
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	#_______ OS ORDERS _______
	os.system("echo off") #Delete @
	os.system("cls") # Clear terminal
	#_________________________


	#================== OPENING TEXT ==========================
	print(yellow(str("""
	_____                     _
	|  __ \                   | |
	| |  \/ __ _ _ __ ___   __| | ___  _ __ ___
	| | __ / _` | '_ ` _ \ / _` |/ _ \| '_ ` _ ``
	| |_\ \ (_| | | | | | | (_| | (_) | | | | | |
	 \____/\__,_|_| |_| |_|\__,_|\___/|_| |_| |_|

	     ~~~ Developed by Ivan Achille ~~~

	"""), style='bold'))
	#=================================================================

	#======================= Coin Sistem =============================
	db_rol_name = "rlcs.coins" #Get file name
	get_coins = open(db_rol_name, 'r') #Open file
	read_db = get_coins.read() #Read the file
	coins = int(read_db) #Declare the coins


	#==================================================================

	########################### Show Coins ###################################
	print(green("▬▬▬▬▬▬▬▬▬▬▬▬▬ Your Balance ▬▬▬▬▬▬▬▬▬▬▬▬▬", style="bold"))
	print("")
	print(white("In G-Coins: "+str(coins), style='bold'))
	cdollar = int(coins)/1000
	print(white("In Dollars: $"+str(cdollar), style='bold'))
	print("")
	print(green("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬", style="bold"))
	###########################################################################


	###################################################################################
	if int(coins)==0:
	    print(red("ERROR: You cant bet, you have not founds.",style="bold"))   #If you have 0 coins the script will auto-exit
	    exit()
	###################################################################################


	#============================+++== COLOR CHOOSE  ======================================
	os.system("cls")
	print(yellow(str("""
	_____                     _
	|  __ \                   | |
	| |  \/ __ _ _ __ ___   __| | ___  _ __ ___
	| | __ / _` | '_ ` _ \ / _` |/ _ \| '_ ` _ ``
	| |_\ \ (_| | | | | | | (_| | (_) | | | | | |
	 \____/\__,_|_| |_| |_|\__,_|\___/|_| |_| |_|

	     ~~~ Developed by Ivan Achille ~~~

	"""), style='bold'))
	print(green("▬▬▬▬▬▬▬▬▬▬▬▬▬ Your Balance ▬▬▬▬▬▬▬▬▬▬▬▬▬", style="bold"))
	print("")
	print(white("In G-Coins: "+str(coins), style='bold'))
	cdollar = int(coins)/1000
	print(white("In Dollars: $"+str(cdollar), style='bold'))
	print("")
	print(green("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬", style="bold"))
	print("")
	print(green(" ▀▄▀▄ ▀ ▄▀ ▄ ▀▄  Choose a color ▀▄▀▄ ▀ ▄▀ ▄ ▀▄ "))
	print("")
	print(white(str("♠ 1) Green X14 "), bg='green', style='bold'))
	print(white(str("♠ 2) Blue X2   "), bg='blue', style='bold'))
	print(white(str("♠ 3) Red  X2   "), bg='red', style='bold'))
	print("")
	colorchoose = str(input(yellow("Color: ")))
	while True:
	    if colorchoose=="1":
	        color = "green"
	        break
	    elif colorchoose=="2":
	        color = "blue"
	        break
	    elif colorchoose=="3":
	        color = "red"
	        break
	    else:
	        print(red("ERROR: Wrong Option",style="bold"))
	        colorchoose = str(input(yellow("Color: ")))
	        print("")

	#============================== END COLOR CHOOSE ======================================


	#============================== BET SISTEM ===========================================


	os.system("cls")
	print(yellow(str("""
	_____                     _
	|  __ \                   | |
	| |  \/ __ _ _ __ ___   __| | ___  _ __ ___
	| | __ / _` | '_ ` _ \ / _` |/ _ \| '_ ` _ ``
	| |_\ \ (_| | | | | | | (_| | (_) | | | | | |
	 \____/\__,_|_| |_| |_|\__,_|\___/|_| |_| |_|

	     ~~~ Developed by Ivan Achille ~~~

	"""), style='bold'))
	print(green("▬▬▬▬▬▬▬▬▬▬▬▬▬ Your Balance ▬▬▬▬▬▬▬▬▬▬▬▬▬", style="bold"))
	print("")
	print(white("In G-Coins: "+str(coins), style='bold'))
	cdollar = int(coins)/1000
	print(white("In Dollars: $"+str(cdollar), style='bold'))
	print("")
	print(green("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬", style="bold"))
	print("")
	print(green(" ▀▄▀▄ ▀ ▄▀ ▄ ▀▄  $$ Make your bet $$ ▀▄▀▄ ▀ ▄▀ ▄ ▀▄ "))
	print("")

	bet = input(yellow("Bet: "))
	while True:
	    if int(bet)>int(coins):
	        print(red("ERROR: Insufficient Coins",style="bold"))
	        bet = input(yellow("Bet: "))
	    elif int(coins)>int(bet):
	        break
	    elif int(coins)==int(bet):
	        break
	coins = int(coins)-int(bet)
	progreso = 0
	cicle_numbers = 50
	os.system("cls") #Clear the terminal
	print(yellow(str("""
	_____                     _
	|  __ \                   | |
	| |  \/ __ _ _ __ ___   __| | ___  _ __ ___
	| | __ / _` | '_ ` _ \ / _` |/ _ \| '_ ` _ ``
	| |_\ \ (_| | | | | | | (_| | (_) | | | | | |
	 \____/\__,_|_| |_| |_|\__,_|\___/|_| |_| |_|

	     ~~~ Developed by Ivan Achille ~~~

	"""), style='bold'))
	print("")
	print(green("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", style="bold"))
	print("Roulette ==> "+"You bet",bet,"to",color)
	print(green("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", style="bold"))
	print("")
	print("")
	#============================ END BET SISTEM =====================================


	#+++++++++++++++++++++++ PICKER SISTEM +++++++++++++++++++++++++
	while True:
	    picker = random.randrange(0,10)


	    if picker==1:
	        picker = white(str(picker), bg='red', style='bold')
	        roullete_result = "red"
	    elif picker==0:
	        picker = white(str(picker), bg='green', style='bold')
	        roullete_result = "green"
	    elif picker==2:
	        picker = white(str(picker), bg='green', style='bold')
	        roullete_result = "green"
	    elif picker==3:
	        picker = white(str(picker), bg='red', style='bold')
	        roullete_result = "red"
	    elif picker==4:
	        picker = white(str(picker), bg='red', style='bold')
	        roullete_result = "red"
	    elif picker==5:
	        picker = white(str(picker), bg='red', style='bold')
	        roullete_result = "red"
	    elif picker==6:
	        picker = white(str(picker), bg='blue', style='bold')
	        roullete_result = "blue"
	    elif picker==7:
	        picker = white(str(picker), bg='blue', style='bold')
	        roullete_result = "blue"
	    elif picker==8:
	        picker = white(str(picker), bg='blue', style='bold')
	        roullete_result = "blue"
	    elif picker==9:
	        picker = white(str(picker), bg='blue', style='bold')
	        roullete_result = "blue"
	    progreso += 1
	    print(yellow("\rResult ==> ")+str(picker), end="")
	    time.sleep(0.1)
	    if progreso>50:
	        break

	#+++++++++++++++++++++++  END PICKER SISTEM +++++++++++++++++++++++++


	#$$$$$$$$$$$$$$$$$$ RESULTS $$$$$$$$$$$$$$$$$$$$$$$$$$

	if color == roullete_result:
	    if roullete_result=="blue":
	        coins_win = int(bet)*2
	    elif roullete_result=="red":
	        coins_win = int(bet)*2
	    elif roullete_result=="green":
	        coins_win = int(bet)*16
	    print()
	    windollar = int(coins_win)/1000
	    print(white("\nRoulette: You win! "+"+"+str(coins_win)+" coins"+" ($"+str(windollar)+")", style="bold", bg="green"))

	    coins = int(coins)+int(coins_win)
	    addcoins = open(db_rol_name, 'w+')
	    addcoins.write(str(coins))

	else:
	    print()
	    betdollar = int(bet)/1000
	    print(white("\nRoulette: You lose! "+"-"+bet+" coins"+" ($"+str(betdollar)+")", style="bold", bg="red"))
	    addcoins = open(db_rol_name, 'w+')
	    addcoins.write(str(coins))
print("")
game()
import os
import time
import random
from colorama import init
from colors import red, green, blue, white, black, yellow
init()
while True:
	ask_restart = input(green("♠ Do you want to restart Y/N: ",style="bold"))
	if str(ask_restart)=="y":
		game()
	elif str(ask_restart)=="Y":
		game()
	elif str(ask_restart)=="n":
		exit()
	elif str(ask_restart)=="N":
		exit()
	else:
		print(red("ERROR: Wrong Option",style="bold"))

#$$$$$$$$$$$$$$$$$$ RESULTS $$$$$$$$$$$$$$$$$$$$$$$$$$
