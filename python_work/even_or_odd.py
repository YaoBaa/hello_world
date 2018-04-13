number = input('Enter a number, and I`ll tell you if it`s even or odd: ')
number = int(number)

if number % 2 == 0:
	print('\nThe number ' + str(number) + ' is even.')
else:
	print('\nThe number ' + str(number) + ' is odd.')


prompt = '\nIt is write by liyaoyao.'
prompt += '\nPlease input your number: '
number = input(prompt)
number = int(number)
if number % 10 == 0:
	print('Yes')
else:
	print('No')
