import hashlib
import os
from colorama import Fore, Back, Style
from time import sleep
import click
from pyfiglet import Figlet



os.system('clear')


# toLog = int(raw_input("Would you like to enable logging? (Hasher will log hashes to a file controlled on local host machine.) [0] for yes [1] for no "))
# print("\n")

# if toLog == int(0):
	# Log = open("hasherLog", "x")
# if toLog == int(1):

@click.command()
# options
# @click.option('--algo', '-a')
def main():
	f = Figlet(font='slant')
	print f.renderText('Hasher')	

	print(" \n")

	toHash = raw_input("Press enter to continue.")

	print(" \n")


	print("\n")
	os.system('clear')

	f = Figlet(font='slant')
	print f.renderText('Hasher')


	CofHash = int(input("-[1]- sha1 \n-[2]- md5 \n-[3]- sha224 \n-[4]- sha256 \n-[5]- sha384 \n-[6]- sha512 " + "\n" +"\n" +"Choose an algorithm: "))
	print("\n")

	# Python ask user for input
	msg = raw_input("Enter text: ")

	print("\n")

	sleep(1)


	if CofHash == int(1):
		hsh = hashlib.sha1(msg)
		hsh.update(msg.encode('utf-8'))
		print("SHA1 hash: " + Fore.RED + hashlib.sha1(msg).hexdigest())
	elif CofHash == int(2):
		hsh = hashlib.md5(msg)
		hsh.update(msg.encode('utf-8'))
		print("MD5 hash: " + Fore.RED + hashlib.md5(msg).hexdigest())
	elif CofHash == int(3):
		hsh = hashlib.sha224(msg)
		hsh.update(msg.encode('utf-8'))
		print("SHA224 hash: " + Fore.RED + hashlib.sha224(msg).hexdigest())
	elif CofHash == int(4):
		hsh = hashlib.sha256(msg)
		hsh.update(msg.encode('utf-8'))
		print("SHA256 hash: " + Fore.RED + hashlib.sha256(msg).hexdigest())
	elif CofHash == int(5):
		hsh = hashlib.sha384(msg)
		hsh.update(msg.encode('utf-8'))
		print("SHA384 hash: " + Fore.RED + hashlib.sha384(msg).hexdigest())
	elif CofHash == int(6):
		hsh = hashlib.sha512(msg)
		hsh.update(msg.encode('utf-8'))
		print("SHA512 hash: " + Fore.RED + hashlib.sha512(msg).hexdigest())

	print Fore.RESET

	print("\n")
	again = raw_input("Would you like to hash another string? Yes [Y] or No [N]")
	if again == ("Y"):
		return main()
	elif again == ("y"):
		os.system('clear')
		return main()



if __name__ == "__main__":
	main()
