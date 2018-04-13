cars = ['ad','bm','bc','ms','fl']
car_1 = 'bs'
car_2 = 'ms'
number_1=10

print(car_1 == 'bs')
print(car_2 != 'bs')

print(car_1.upper() == 'BS')

print(number_1 == 10)
print(number_1 != 11)
print(number_1 > 9)
print(number_1 < 11)
print(number_1 >= 10)
print(number_1 <= 10)

print((number_1 == 10) and (car_1 == 'ms'))
print((number_1 == 10) or (car_1 == 'ms'))

print(car_1 in cars)
print(car_2 in cars)

print(car_1 not in cars)
print(car_2 not in cars)

print('lb' in cars)
print('lb' not in cars)
