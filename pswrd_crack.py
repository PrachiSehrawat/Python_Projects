######################## PASSWORD CRACKER ##############################

import hashlib

flag = 0

pass_hash = input("Enter md5 Hash: ")
wordlist = input("Enter File Name: ")

try:
	pass_file = open(wordlist, "r")

except:
	print("File Not Found")
	quit()

for word in pass_file:
	enc_wrd = word.encode("utf-8")
	digest = hashlib.md5(enc_wrd.strip()).hexdigest()

	if digest == pass_hash:
		print("Password has been found")
		print("Password is"+word)
		flag = 1
		break

if flag == 0:
	print("Password is not in the list")





