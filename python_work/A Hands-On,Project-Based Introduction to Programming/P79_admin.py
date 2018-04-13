users = ['admin','root','tiger','mini','python']
for user in users:
	if user == 'admin' or user =='root':
		print('Hello '+user+',would you like to see a status report?')
	else:
		print('Hello '+user+',welcome to the system.')
print('\n')

users = []
if users:	
	for user in users:	
		if user == 'admin' or user =='root':
			print('Hello '+user+',would you like to see a status report\
			?')
		else:
			print('Hello '+user+',welcome to the system.')
else:
		print('No user!')
print('\n\n\n')

current_users = ['admin','root','tiger','Mini','python']
current_usersed = [current_user.lower() for current_user in current_users]
new_users = ['a','b','Python','mini','e']
for new_user in new_users:
	if new_user.lower() not in current_usersed:
		print(new_user+' is not exist.')
	else:
		print('\t'+new_user+'is exist.')
		
numbers = list(range(1,10))
for number in numbers:
	if number == 1:
		print(str(number)+'st'+'\n')
	elif number == 2:
		print(str(number)+'nd'+'\n')
	elif number == 3:
		print(str(number)+'rd'+'\n')
	else:
		print(str(number)+'th'+'\n')

