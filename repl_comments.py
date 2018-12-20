all_comments = ''
order = 1
def comments(n):
	global all_comments, order
	if n == '':
		print('Done.')
		return False
	else:
		all_comments += '\n' + str(order) + '.' + ' ' + str(n)
		print('Previously entered comments: ',all_comments)
		order += 1
		return True 	
while True:
	n = str(input('Enter your comment(press enter to quit): '))
	type_comment = comments(n)	
	if type_comment == False:
		break
