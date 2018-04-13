#coding=utf-8
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

new_points = alien_0['points']
print('You just earned '+str(new_points)+' points')

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print('\n')

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print("old color is "+alien_0['color'])
alien_0['color'] = 'yellow'
print("new color is "+alien_0['color']+'\n\n\n')

#向右移动外星人
alien_0 = {}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'
print(alien_0)
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(alien_0)
print('\n')

aliens = {'color':'yellow','points':10,'speed':'medium','test':'test'}
print(aliens)
del aliens['test']
print(aliens)
