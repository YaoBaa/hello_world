#coding=utf-8
current_number = input('Input your number: ')
current_number = int(current_number)
while current_number <= 100:
	print(current_number)
	current_number += 1

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue #放弃后续代码，返回循环开头
	print(current_number)

x = 1
while x < 5:
	print(x)
