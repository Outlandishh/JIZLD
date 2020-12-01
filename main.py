from hashlib import md5, sha256, sha512
from os import system, name, path
from time import sleep

system("title Main")
match = False
hash_file = "resources/hashes.txt"
verbose_mode = False

def hashType(selection, line):
	if selection == "1":
		digest = md5(bytes(line, 'utf8')).hexdigest()
	elif selection == "2":
		digest = sha256(bytes(line, 'utf8')).hexdigest()
	elif selection == "3":
		digest = sha512(bytes(line, 'utf8')).hexdigest()
	else:
		print("\n[\u001b[31m!\u001b[0m]Invalid option.")
		sleep(3)
		main()
	return digest

def hashLookupCheck(src, header, file):
	if path.exists(file) == False:
		print("[\u001b[31m!\u001b[0m]Must create hash lookup first.")
		sleep(5)
		hasher(src)
	else:
		selection = input("Create hash lookup?[y/n]")
		if selection == "y":
			hasher(src)
		elif selection != "n":
			print("[\u001b[31m!\u001b[0m]Invalid input.")
			sleep(3)
			main()
	clear()
	print(header)

def passwordSecurityScore(password):
	password_comment = "Highly secure password"
	password_variation_score = 0.8
	
	number_check = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	capital_check = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	punctuation_check = [',', '<', '.', '>', '/', '?', ';', ':', '"', "'", '[', ']', '{', '}', '-', '=', '_', '+', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

	if any(char in password for char in number_check):
		password_variation_score += 0.15
	if any(char in password for char in punctuation_check):
		password_variation_score += 0.15
	if any(char in password for char in capital_check):
		password_variation_score += 0.10

	password_length_score = int(len(password)) / 4.5
	password_security_score = pow(password_length_score, 2.7) * password_variation_score + 1

	if password_security_score > 10:
		password_security_score = 10
	elif password_security_score > 8:
		password_comment = "Very secure password"
	elif password_security_score > 7:
		password_comment = "Strong password"
	elif password_security_score > 6:
		password_comment = "Moderate password"
	elif password_security_score > 4:
		password_comment = "Weak password!"
	else:
		password_comment = "Why bother having a password..."

	print("Password Score: " + str(password_security_score) + " - " + password_comment)

def fileLen(fname):
    with open(fname, errors="ignore") as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def clear(): 
	if name == 'nt':
		system('cls')
	else:
		system('clear')

def hasher(src):
	clear()
	global verbose_mode
	print("\tHasher\n======================\n[1] MD5\n[2] sha256\n[3] sha512")

	hash_type = input("Hash Algorithm: ")

	password_file = input("Password File Location[Default: resources/passwords.txt]: ")
	if password_file == "":
		password_file = "resources/passwords.txt"
	if path.exists(password_file) == False:
		print("\n[\u001b[31m!\u001b[0m]Invalid file.")
		sleep(3)
		main()

	hash_file = input("Hash File Location[Default: resources/hashes.txt]: ")
	if hash_file == "":
		hash_file = "resources/hashes.txt"
	if path.exists(hash_file) == False:
		print("\n[\u001b[31m!\u001b[0m]File does not exist.\n")
		sleep(3)

	try:
		salt = False
		salt_selection = input("Do you wish to salt?[y/n]").lower()
		if salt_selection == "y":
			salt = True
		elif salt_selection != "n":
			print("[\u001b[31m!\u001b[0m]Invalid input.")
			sleep(3)
			main()
	except:
		print("[\u001b[31m!\u001b[0m]Invalid input.")
		sleep(3)
		main()
		
	print("\nReading file contents...")

	if verbose_mode == True:
		file_len = fileLen(password_file)
	write_file = open(hash_file, 'w')

	print("File contents read.\n\nStarting Hash...")
	
	count = 0
	for line in open(password_file, errors="ignore"):
		if salt == True:
			line += "!Salt!"
		digest = hashType(hash_type, line[:-1])
		write_file.write(digest + '\n')
		count += 1
		if (count/1000000).is_integer() and verbose_mode == True:
			print(str("%.2f" % (100/(file_len/count))) + "%")
	
	print("\nHash Completed!")
	write_file.close()
	print("File saved!")
	sleep(3)

def passwordTest():
	clear()
	global verbose_mode
	global match
	match = False
	global hash_file
	global password_file
	
	header = "\tPassword Test\n=============================="
	print(header)

	hashLookupCheck("passwordTest", header, hash_file)

	txt_input = input("Password: ")
	hash_type = input("[1] MD5\n[2] sha256\n[3] sha512\nHash Algorithm: ")
	md5_input = hashType(hash_type, txt_input)
	hash_file = input("Hash File Location[Default: resources/hashes.txt]: ")

	if hash_file == "":
		hash_file = "resources/hashes.txt"
	if path.exists(hash_file) == False:
		print("\n[\u001b[31m!\u001b[0m]Invalid file.")
		sleep(3)
		main()
	if verbose_mode == True:
		print("\nReading file contents...")
		file_len = fileLen(hash_file)
		print("File contents read.")
	
	print("\nStarting test...")
	
	count = 0
	for line in open(hash_file, errors="ignore"):
		line = line[:-1]
		if md5_input == line:
			write_file = open('comparison_output.txt', 'w')
			write_file.write(line + " = " + txt_input)
			write_file.close()
			print("\n[\u001b[31m!\u001b[0m]Comparison found: " + line + " = " + txt_input)
			match = True
			break
		count += 1
		if (count/1000000).is_integer() and verbose_mode == True:
			print(str("%.2f" % (100/(file_len/count))) + "%")

	if match == False:
		print("\nNo Match Found.")
		passwordSecurityScore(txt_input)
	sleep(5)

def hashCompare():
	clear()
	global verbose_mode
	global match
	match = False
	global hash_file
	global password_file

	header = "\tHash Comparison\n==============================="
	print(header)
	
	hashLookupCheck("hashCompare", header, hash_file)

	txt_input = input("Hash: ")
	
	password_file = input("Password File Location[Default: resources/passwords.txt]: ")
	if password_file == "":
		password_file = "resources/passwords.txt"
	if path.exists(password_file) == False:
		print("\n[\u001b[31m!\u001b[0m]Invalid file.")
		sleep(3)
		main()

	hash_file = input("Hash File Location[Default: resources/hashes.txt]: ")
	if hash_file == "":
		hash_file = "resources/hashes.txt"
	if path.exists(hash_file) == False:
		print("\n[\u001b[31m!\u001b[0m]Invalid file.")
		sleep(3)
		main()

	if verbose_mode == True:
		print("\nReading file contents...")
		file_len = fileLen(hash_file)
		print("File contents read.")
	print("\nStarting comparison...")

	count = 0
	for line in open(hash_file, errors="ignore"):
		line = line[:-1]
		if txt_input == line:
			with open(password_file) as f:
				for x, line in enumerate(f):
					if x == count:
						password = line
						break
			write_file = open('comparison_output.txt', 'w')
			write_file.write(line + " = " + password)
			write_file.close()
			print("\nPassword found: " + line + " = " + password)
			match = True
			break
			count += 1
			if (count/1000000).is_integer() and verbose_mode == True:
				print(str("%.2f" % (100/(file_len/count))) + "%")
	
	if match == False:
		print("\nNo Match Found.")
	sleep(3)

def main():
	clear()
	global verbose_mode
	print("\tSelect an option:\n=================================\n[1] Hasher\n[2] Password Security Check\n[3] Hash Comparison\n[4] Enable Verbose Mode\n[0] Exit\n=================================")
	selection = input("Option: ")

	if selection == "1":
		hasher("main")
	elif selection == "2":
		passwordTest()
	elif selection == "3":
		hashCompare()
	elif selection == "4":
		verbose_mode = True
		print("Verbose mode enabled")
		sleep(2)
	elif selection == "0":
		exit()
	else:
		print("\n[\u001b[31m!\u001b[0m]Please enter a valid input.")
		sleep(3)
	clear()
	main()

main()
