users = {
	'aeinstein':{
		'first':'albert',
		'last':'einstein',
		'location':'princeton',
		},
	'mcurie':{
		'first':'marie',
		'last':'curie',
		'location':'paris',
		},
	}
for username,user_info in users.items():
	print('\nUsername: ' + username)
	full_name=user_info['first'] + ' ' + user_info['last']
	
	print('\tFull name: ' + full_name.title())
	print('\tLocation: ' + user_info['location'].title())
	

