bicycles=['trek','cannondale','redline','specialized']
print(bicycles[-1].upper())

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='ducati'#修改列表元素
print(motorcycles)

motorcycles.append('honda')#在列表末尾添加元素
print(motorcycles)


motorcycles=[]
print(motorcycles)
motorcycles.append("honda")
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0,'ducati')#在第0位插入一个元素
print(motorcycles)

del motorcycles[0]#删除第0位元素
print(motorcycles)

del motorcycles[1]
print(motorcycles)
print("\n")

print(bicycles)
popped_bicycle=bicycles.pop()#删除列表末尾元素并赋值给popped_bicycles
print(bicycles)
print(popped_bicycle)
second_bicycle=bicycles.pop(1)#删除列表第二个元素并赋值给second_bicycle
print(bicycles)
print(second_bicycle)
print("\n")

bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
bicycles.remove('redline')#根据值删除元素（只能删除第一个指定的值）
print(bicycles)
print("\n")

cars=['bmw','audi','toyota','subaru']
print(cars)
cars.sort()#按字母永久排序
print(cars)
cars.sort(reverse=True)#按字母相反顺序排序
print(cars)
print("\n")

cars=['bmw','audi','toyota','subaru']
print(sorted(cars))#对列表进行临时排序
print(cars)
cars.reverse()#永久性反序排列列表，和以前顺序相反，与其他因素无关
print(cars)
print(len(cars))
