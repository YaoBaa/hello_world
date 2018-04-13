#coding=utf-8
def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())
	

def make_great(magicians):
	magician = ""
	while magicians:
		magician = magicians.pop() + " The Great"
		magicians_linshi.append(magician)
	magicians = magicians_linshi[:]
	return(magicians)
magicians = ['anna','hebao','xue']
magicians_linshi = []
make_great(magicians)
magicians = magicians_linshi[:]
#magicians = make_great(magicians)#´Ómake·µ»Ø
show_magicians(magicians)
show_magicians(magicians_linshi)


