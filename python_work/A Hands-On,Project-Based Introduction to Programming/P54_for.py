#4-3
print('4-3')
a=[]
for values in range(1,21):
	a.append(values)
print(a)
b=[values for values in range(1,11)]
print(b)
print('\n')

#4-4
print('4-4')
c=[values for values in range(1,11)]
for value in c:
	print(value)
print('\n')

#4-5
print('4-5')
d=list(range(1,1000001))
print(min(d))
print(max(d))
print(sum(d))
print('\n')

#4-6
print('4-6')
e=[values for values in range(1,20,2)]
for value in e:
	print(value)
print('\n')

#4-7
print('4-7')
f=list(range(3,31,3))
for value in f:
	print(value)
print('\n')

#4-8
print('4-8')
g=[]
for value in range (1,11):
	g.append(value**3)
print(g)
print('\n')

#4-9
print('4-9')
h=list(value**3 for value in range(1,11))
print(h)
