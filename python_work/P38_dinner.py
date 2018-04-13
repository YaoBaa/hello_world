guests=['pp','hb','bb','mm']
print(guests)

#3.5
print(guests[0].title()+" is somewhere else.")

del guests[0]
guests.insert(0,'nn')
print(guests)

print("\tWelcome "+guests[0].title()+" to dinner!")
print("\tWelcome "+guests[1].title()+" to dinner!")
print("\tWelcome "+guests[2].title()+" to dinner!")
print("\tWelcome "+guests[-1].title()+" to dinner!")

#3.6
print("\nI found a bigger dining-table!")
guests.insert(0,'dd')
guests.insert(2,'2')
guests.insert(-1,'last')
guests.insert(-1,'last2')
print(guests)
print("\n")

#3.7
pop_1=guests.pop(2)
print("sorry to "+pop_1)
pop_1=guests.pop(2)
print("sorry to "+pop_1)
pop_1=guests.pop(2)
print("sorry to "+pop_1)
pop_1=guests.pop(2)
print("sorry to "+pop_1)
pop_1=guests.pop(2)
print("sorry to "+pop_1)
pop_1=guests.pop(2)
print("sorry to "+pop_1)
print(guests)

del guests[0]
del guests[0]
print(guests)
