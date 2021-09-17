import hashlib
import os
from colorama import Fore, Back, Style
from time import sleep
import click
from pyfiglet import Figlet

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


		try:
			CofHash = int(input("-[1]- sha1 \n-[2]- md5 \n-[3]- sha224 \n-[4]- sha256 \n-[5]- sha384 \n-[6]- sha512 " + "\n" +"\n" +"Choose an algorithm: "))
			print("\n")
		except(ValueError):
			CofHash = int(input("Please enter a number!"))



		


		# Python ask user for input
		msg = input("Enter text: ")

		print("\n")

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
		again = input("Would you like to hash another string? Yes [Y] or No [N]")
		if again == ("Y"):
			return main()
		elif again == ("y"):
			os.system('clear')
			return main()

	return repeat()







if __name__ == "__main__":
	main()

