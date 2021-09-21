import hashlib
import os
from colorama import Fore, Back, Style
from time import sleep
import click
from pyfiglet import Figlet
import getpass


os.system('clear')

@click.command()
# options
# @click.option('--algo', '-a')
def main():
	f = Figlet(font='slant')
	print(f.renderText('Hasher'))	
	print(' \n')
	toHash = input("Press enter to continue.")
	print(' \n')

	def repeat():
		
		print('\n')
		os.system('clear')

		f = Figlet(font='slant')
		print(f.renderText('Hasher'))

		def choices():
			print("-[1]- sha1 \n-[2]- md5 \n-[3]- sha224 \n-[4]- sha256 \n-[5]- sha384 \n-[6]- sha512 " + "\n" +"\n")

		choices()

		def error():

			try:
				global CofHash
				CofHash = int(input("\nChoose an algorithm: "))
				print("\n")
			except(ValueError):
				print("\nPlease enter a number! \n")

				sleep(1)
				
				# CofHash = int(input("Choose an algorithm: "))
				try:
					int(input("Choose an algorithm: "))
				except(ValueError):
					os.system('clear')
					print(f.renderText('Hasher'))
					choices()
					error()



		try:
			error()
		except(ValueError):
			error()



		# Python ask user for input
		# msg = input("Enter text: ")
		os.system('clear')
		print(f.renderText('Hasher'))

		# algo tag
		def tag():
			if CofHash == 1:
				print(Back.RED + Fore.Black + "sha1")
			elif CofHash == 2:
				print(Back.RED + Fore.BLACK + "md5")
			elif CofHash == 3:
				print(Back.RED + Fore.BLACK + "sha224")
			elif CofHash == 4:
				print(Back.RED + Fore.BLACK + "sha256")
			elif CofHash == 5:
				print(Back.RED + Fore.BLACK + "sha384")
			elif CofHash == 6:
				print(Back.RED + Fore.BLACK + "sha512")


		tag()

		print(Fore.RESET + Back.RESET)



		msg = getpass.getpass("Enter text: ")

		print("\n")

		os.system('clear')
		print(f.renderText('Hasher'))

		sleep(1)


		if CofHash == int(1):
			enmsg = msg.encode('utf-8')
			hsh = hashlib.sha1(enmsg)			
			print("SHA1 hash: " + Fore.RED + hashlib.sha1(enmsg).hexdigest())
		elif CofHash == int(2):
			enmsg = msg.encode('utf-8')
			hsh = hashlib.md5(enmsg)			
			print("MD5 hash: " + Fore.RED + hashlib.md5(enmsg).hexdigest())
		elif CofHash == int(3):
			enmsg = msg.encode('utf-8')
			hsh = hashlib.sha224(enmsg)			
			print("SHA224 hash: " + Fore.RED + hashlib.sha224(enmsg).hexdigest())
		elif CofHash == int(4):
			enmsg = msg.encode('utf-8')
			hsh = hashlib.sha256(enmsg)			
			print("SHA256 hash: " + Fore.RED + hashlib.sha256(enmsg).hexdigest())
		elif CofHash == int(5):
			enmsg = msg.encode('utf-8')
			hsh = hashlib.sha384(enmsg)			
			print("SHA384 hash: " + Fore.RED + hashlib.sha384(enmsg).hexdigest())
		elif CofHash == int(6):
			enmsg = msg.encode('utf-8')
			hsh = hashlib.sha512(enmsg)			
			print("SHA512 hash: " + Fore.RED + hashlib.sha512(enmsg).hexdigest())

		print(Fore.RESET)

		print("\n")
		again = input("Would you like to hash another string? Yes [Y] or No [N] \n")
		if again == ("Y"):
			return main()
		elif again == ("y"):
			os.system('clear')
			return main()

	return repeat()







if __name__ == "__main__":
	main()

