import random
import numpy as np

def generate_password(

    password_length: int = 8,

    has_symbols: bool = False,

    has_uppercase: bool = False,
    
    ignored_chars: list = [],
    
    allowed_chars: list = []) -> str:
	
	
	"""Generates a random password.

	The password will be exactly `password_length` characters.

	If `has_symbols` is True, the password will contain at least one symbol, such as #, !, or @.

	If `has_uppercase` is True, the password will contain at least one upper case letter.
	
	If `ignored_chars` is input then the characters in the ignored_chars list will not be in the password.
	
	If `allowed_chars` is input the password will only contain characters from the allowed_chars list.
	
	"""

	password = []
	special_letters = "#!@\\\"/.,;'#:~£$%^&*()_+-={}[]"
	upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	lower_letters = "abcdefghijklmnopqrstuvwxyz1234567890"
	allowed_flag = False
	
	if ignored_chars != [] and allowed_chars != []:
		raise UserWarning("You can only input one of either: ignored_chars or allowed_chars!")
	
	elif ignored_chars != []:
		for char in ignored_chars:
			special_letters = special_letters.replace(char,"")
			upper_letters = upper_letters.replace(char,"")
			lower_letters = lower_letters.replace(char,"")
				
	
	elif allowed_chars != []:
		allowed_flag = True
		
	else:
		pass

	if allowed_flag:
		for i in range(0, password_length):
			password.append(random.choice(allowed_chars))
	
	elif has_symbols and not has_uppercase:
		password.append(random.choice(special_letters))
		rand_list = lower_letters + special_letters
		password_length -= 1
		for i in range(0,password_length):
			password.append(random.choice(rand_list))

	elif has_uppercase and not has_symbols:
		password.append(random.choice(upper_letters))
		rand_list = lower_letters + upper_letters
		password_length -= 1
		for i in range(0,password_length):
			password.append(random.choice(rand_list))

	elif has_uppercase and has_symbols:
		password.append(random.choice(special_letters))
		password.append(random.choice(upper_letters))
		rand_list = special_letters + upper_letters + lower_letters
		password_length -= 2
		for i in range(0,password_length):
			password.append(random.choice(rand_list))

	else:
		for i in range(0,password_length):
			password.append(random.choice(lower_letters))

	np.random.shuffle(password)
	password = "".join(password)
	return password
