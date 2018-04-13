#6-7
hb = {'last_name':'zhu',
	'first_name':'hui',
	'age':22,
	'city':'shaoxin',
	}
mm = {'last_name':'luo',
	'first_name':'rong',
	'age':46,
	'city':'jingzhou',
	}
bb = {'last_name':'li',
	'first_name':'yi',
	'age':47,
	'city':'jingzhou',
	}
people = [hb,mm,bb]

for name in people:
	print(name)
	for keys in name:
		print('\t' + keys + ': ' +str(name[keys]))
print('\n')
print('\n')
print('\n')

#6-9
favorite_places = {
	'hb':['qingdao','shaoxin','hangzhou'],
	'mm':['jingzhou','nanjing','shashi'],
	'bb':['lixian','zhangzhuang','nanping'],
	}
for keys,values in favorite_places.items():
	print(keys.title() + '`s favorite places are:')
	for place in values:
		print(place.title())
	print('\n')

#6-11
cities = {
	'jingzhou':{
		'people':1000000,
		'country':'China',
		'others':'hometown',
		},
	'nanjing':{
		'people':2000000,
		'country':'China',
		'others':'university',
		},
	'shaoxin':{
		'people':1200000,
		'country':'China',
		'others':'like',
		},
	}
for city in cities.keys():
	print(city.title()+':')
	for keys,values in cities[city].items():
		print(keys + ': ' + str(values))
	print('\n')
