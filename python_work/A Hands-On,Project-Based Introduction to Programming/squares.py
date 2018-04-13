squares=[]
for value in range(2,13,2):
	square=value**2
	squares.append(square)
print(squares)

squares=list(range(1,6))
for a in squares:
	print(a)
	squares.remove(a)
print(squares)
for value in range(0,100,10):
	squares.append(value**2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares));
