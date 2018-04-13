file_name_1 = 'cats.txt'
file_name_2 = r'F:\ython_work\dogs.txt'

try:
	with open(file_name_1) as file_obj_1:
		file_1 = file_obj_1.read()
		print(file_1)
	with open(file_name_2) as file_obj_2:
		for line in file_obj_2:
			print(line.rstrip())
except FileNotFoundError:
	#print("File Not Found")
	pass
