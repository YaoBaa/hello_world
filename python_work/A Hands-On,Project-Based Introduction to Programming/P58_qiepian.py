cuts=list(range(2,20,3))
print('The first three items in the list are:')
print(cuts)
print(cuts[:3])
print(cuts[1:4])
print(cuts[-3:])
print('\n')

cut=cuts[:]
cuts.append('10000')
cut.append('99999')
for values in cuts:
	print(values)
print(cuts)
for values in cut:
	print(values)
print(cut)
