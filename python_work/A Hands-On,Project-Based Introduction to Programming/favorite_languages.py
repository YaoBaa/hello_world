#coding=utf-8
favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
print('Jen`s favorite language is '+
	favorite_languages['jen'].title()+
	'.\n')
	
hb = {'last_name':'hui',
	'first_name':'zhu',
	'age':22,
	'city':'shaoxin',
	}
print(hb)
print('\n')

for key,value in hb.items():
	print("Key: "+key)
	print('Value: '+str(value))
	print(key+': '+str(value))
	print('\n')

for name,language in favorite_languages.items():
	print(name.title()+
		'`s favorite language is '+
		language.upper()+
		'\n'
		)
for name in favorite_languages.keys():#遍历字典中的键，也可删去‘.keys()'，默认遍历键
	print(name.title())
friends = ['jen','phil']
for name in favorite_languages:
	print(name)
	if name in friends:
		print("Hi,"+
			name.title()+
			'!I see your favorite language is '+
			favorite_languages[name].title())
	else:
		print('I do not remember '+name.upper())
		
if 'eric' not in favorite_languages:
	print('please take your poll!')
for name in sorted(favorite_languages.keys()):
	print(name.title()+'\n')
for value in sorted(favorite_languages.values()):
	print(value)

shoulds = ['eric','jen','phil','liyaoyao']
for should in shoulds:
	if should not in favorite_languages.keys():
		print('please,'+should)
	else:
		print('thanks,'+should)

favorite_languages = {
	'jen':['python','java'],
	'sarah':['c','web'],
	'edward':['ruby',],
	'phil':['python','js'],
	}
for name,languages in favorite_languages.items():
	if len(languages) == 1:
		print(name+'`s favoite languages is :')
		for language in languages:
			print('\t'+language.title())
	else:
		print(name+'`s favoite languages are :')
		for language in languages:
			print('\t'+language.title())
