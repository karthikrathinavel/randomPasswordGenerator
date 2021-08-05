import random

chars = "abcdefghijklmnoqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+:;{[]}|'<,.>/?"
password_len = int(input("Enter the length of the password you want: "))
password_count = int(input("How many passwords you want: "))

for x in range(0,password_count):
	password = ""
	for x in range(0,password_len):
		ch = random.choice(chars)
		password = password + ch
	print("password: ",password)