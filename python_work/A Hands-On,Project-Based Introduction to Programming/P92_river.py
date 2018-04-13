python = {'str':'change others to string',
	'range':'make some numbers',
	'pop':'delete and use',
	'append':'add to the end',
	'remove':'delete with keys'}
for key in python.keys():
	print(key+': '+python[key].title())
python['title'] = 'the first to big'
python['lower'] = 'all to small'
python['upper'] = 'all to big'
python['len'] = 'how many'
python['reverse'] = 'the other other'
print('\n')
for key in python.keys():
	print(key+': '+python[key].title())

rivers = {'rivera':'a,b,c',
	'riverb':'A','riverb':'B','riverb':'C'}
for river in rivers.keys():
	if river == 'rivera':
		print(river +' through '+rivers[river])
for country in rivers.values():
	print(country)
