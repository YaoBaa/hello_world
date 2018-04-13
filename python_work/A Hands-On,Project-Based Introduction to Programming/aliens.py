#coding=utf-8
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'red','points':25}
alien_2 = {'color':'yellow','points':25}
alien_3 = {'color':'blue','points':10}
aliens = [alien_0,alien_1,alien_2,alien_3]
for alien in aliens:
	print(alien)
aliens = []
for alien_number in range(30):#随机生成30个
	new_alien = {'color':'blue','points':5,'speed':'slow'}
	aliens.append(new_alien)
for alien in aliens[:5]:
	print(alien)
print('there are '+str(len(aliens))+' aliens\n')

for alien in aliens[:3]:
	alien['color'] = 'red'
	alien['speed'] = 'medium'
	alien['points'] = 10
for alien in aliens[:5]:
	print(alien)
