import random
lower= "abcdefghigklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER= "0123456789"
Symbol= "#@!?"

reason = input('For Which Purpose You Are Generating Password\n[For.. G-Account, Outlook-Account, etc] : ')

all= lower+upper+NUMBER+Symbol
length=8
password= "".join(random.sample(all, length))

print("\nYour Password Is:-\n" + password)

with open('Your_Python_Generated Passwords.txt', 'a') as f:
	f.write(f'\n{reason} Password: {password}')

print('\nYour passwords are stored in text file, it has been stored as \'Your _Python_Generated_Passwords\'')