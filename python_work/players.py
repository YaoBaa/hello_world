players=['charles','martina','michael','florence','eli']
print(players[:4])
for player in players[:3]:
	print(player.title())


my_foods=['pizza','falafel','carrot']
friend_foods=my_foods[:]
print(my_foods)
print(friend_foods)

a=my_foods
print(a)

a.append('ice cream')
print(my_foods)
