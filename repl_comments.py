from hashlib import sha256 #***
all_comments = ''
order = 1
my_hash = 'b1e79532d5b97c775ed657e6aea1de1cb3728443c6b35ad80fa7c3c4ed0f4d1e' #***# i created this hash using code in this site: (https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py)
def create_hash(password): #***
    pw_bytestring = password.encode()  #***
    return sha256(pw_bytestring).hexdigest() #***
    		
def comments(n):
	global all_comments, order
	if n == '':
		print('Done.')
		return False
	else:
		pw = input('Please enter your password:')  # ***
		hsh = create_hash(pw)  #***
		if hsh == my_hash: 
			all_comments += '\n' + str(order) + '.' + ' ' + str(n)
			print('Previously entered comments: ',all_comments)
			order += 1
			return True 
		else:
			print('''I am sorry i can't let you do that.\n!!!!You need to enter correct password!!!!''')		

while True:
	n = str(input('Enter your comment(press enter to quit): '))
	type_comment = comments(n)	
	if type_comment == False:
		break
#when i was making password hashing i borrowed the codes with the stars from here => (https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py).
