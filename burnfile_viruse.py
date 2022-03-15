import os
import time
import sys
import colorama
from termcolor import colored	
from colorama import Fore, Style
from time import sleep

# Python program to print
# colored text and background
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

#prCyan("Hello World, ")
#prYellow("It's")
#prGreen("Geeks")
#prRed("For")
#prGreen("Geeks")

prRed("\t♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️")
prYellow(""" 
		██████                           ████████ ██  ██        
		░█░░░░██                         ░██░░░░░ ░░  ░██        
		░█   ░██  ██   ██ ██████ ███████ ░██       ██ ░██  █████ 
		░██████  ░██  ░██░░██░░█░░██░░░██░███████ ░██ ░██ ██░░░██
		░█░░░░ ██░██  ░██ ░██ ░  ░██  ░██░██░░░░  ░██ ░██░███████
		░█    ░██░██  ░██ ░██    ░██  ░██░██      ░██ ░██░██░░░░ 
		░███████ ░░██████░███    ███  ░██░██      ░██ ███░░██████
		░░░░░░░   ░░░░░░ ░░░    ░░░   ░░ ░░       ░░ ░░░  ░░░░░░ 
			 ██      ██ ██                               
			░██     ░██░░                                
			░██     ░██ ██ ██████ ██   ██  ██████  █████ 
			░░██    ██ ░██░░██░░█░██  ░██ ██░░░░  ██░░░██
			 ░░██  ██  ░██ ░██ ░ ░██  ░██░░█████ ░███████
			  ░░████   ░██ ░██   ░██  ░██ ░░░░░██░██░░░░ 
			   ░░██    ░██░███   ░░██████ ██████ ░░██████
			    ░░     ░░ ░░░     ░░░░░░ ░░░░░░   ░░░░░░ 
""")
prRed("\t♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️♨️")
prPurple("\t\t\t # BURNFILE VIRUSE MADE BY -> YOGESH BAGHEL(CEO)")

print("")
print("")
prGreen("\t\t======================================================================")
prYellow("\t\t|         Burn The Target File with Install Best Viruse Tool         |")
prGreen("\t\t======================================================================")

print()

#prYellow("[ + ]  Use It At Own Your Risk.")
#prYellow("[ + ]  No Warranty")
#prYellow("[ + ]  Use It Legal Purpose Only.")
#prYellow("[ + ]  We Are Not Responsible For Your Action.")
#prYellow("[ + ]  We Do Not Things That Are Forbidden.")
#prYellow("[ + ]  It's damage Your Files.")


print(f"{Fore.YELLOW}\t[ + ] {Style.RESET_ALL}{Fore.BLUE} Use It At Own Your Risk.")
print(f"{Fore.YELLOW}\t[ + ] {Style.RESET_ALL}{Fore.BLUE} No Warranty.")
print(f"{Fore.YELLOW}\t[ + ] {Style.RESET_ALL}{Fore.BLUE} Use It Legal Purpose Only.")
print(f"{Fore.YELLOW}\t[ + ] {Style.RESET_ALL}{Fore.BLUE} We Are Not Responsible For Your Action.")
print(f"{Fore.YELLOW}\t[ + ] {Style.RESET_ALL}{Fore.BLUE} We Do Not Things That Are Forbidden.")
print(f"{Fore.YELLOW}\t[ + ] {Style.RESET_ALL}{Fore.BLUE} It's damage Your Files.")
print()

prRed("\t\tIf you are installing this VIRUSE.")
prRed("\t\tThat means You are agree with all terms.")

print("")
t=input("\tDo you want install Viruse [Y/N]> ")

# Function for implementing the loading animation
def load_animation():

		# String to be displayed when the application is loading
		load_str = "Start Installing BurnFile Viruse....."
		ls_len = len(load_str)


		# String for creating the rotating line
		animation = "|/-\\"
		anicount = 0
		
		# used to keep the track of
		# the duration of animation
		counttime = 0		
		
		# pointer for travelling the loading string
		i = 0					

		while (counttime != 100):
			
			# used to change the animation speed
			# smaller the value, faster will be the animation
			time.sleep(0.175)
								
			# converting the string to list
			# as string is immutable
			load_str_list = list(load_str)
			
			# x->obtaining the ASCII code
			x = ord(load_str_list[i])
			
			# y->for storing altered ASCII code
			y = 0							

			# if the character is "." or " ", keep it unaltered
			# switch uppercase to lowercase and vice-versa
			if x != 32 and x != 46:			
				if x>90:
					y = x-32
				else:
					y = x + 32
				load_str_list[i]= chr(y)
			
			# for storing the resultant string
			res =''			
			for j in range(ls_len):
				res = res + load_str_list[j]
				
			# displaying the resultant string
			sys.stdout.write("\r"+res + animation[anicount])
			sys.stdout.flush()

			# Assigning loading string
			# to the resultant string
			load_str = res

			
			anicount = (anicount + 1)% 4
			i =(i + 1)% ls_len
			counttime = counttime + 1
		
		# for windows OS
		if os.name =="nt":
			os.system("cls")
			
		# for linux / Mac OS
		else:
			os.system("clear")
			
if(t=='y' or t=='Y'):
	load_animation()
	# Insert the directory path in here
	path = '/home/yogesh'
	# Extracting all the contents in the directory corresponding to path
	#l_files = os.listdir(path) 
	# Iterating over all the files
	
	#def print_slowly(text):
		#for c in text:
			#sys.stdout.write(c)
			#sys.stdout.flush()
			#time.sleep(0.1)
			
	mylist=[]
	for x in os.listdir(path):
		mylist.append(x)
		
	#print(mylist,emd="\n")

	for i in range(len(mylist)):
		print(mylist[i])
		sys.stdout.flush()
		time.sleep(0.2)
	
	
	
	#for file in l_files:
	  #Instantiating the path of the file
		#file_path = f'{path}\\{file}'
		#Checking whether the given file is a directory or no
		#if os.path.isfile(file_path):
			#try:
				#Printing the file pertaining to file_path
				#os.startfile(file_path, 'print')
				#print(f'Printing {file}')
				#Sleeping the program for 5 seconds so as to account the 
		  #steady processing of the print operation.
				#time.sleep(5)
			#except:
				#Catching if any error occurs and alerting the user
				#print(f'ALERT: {file} could not be printed! Please check\the associated softwares, or the file type.')
		#else:
			#print(f'ALERT: {file} is not a file, so can not be printed!')
	#print('Task finished!')

	

		# Your desired code continues from here
		# s = input("Enter your name: ")
		#s =[""]
		#sys.stdout.write(""+str(s)+"\n")
		
else:
	#exit()
	# for windows
	if os.name =="nt":
			os.system("cls")
			
	# for linux / Mac OS
	else:
		os.system("clear")
