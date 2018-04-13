def city_country(city,country):
	print('"' + city + ',' + country + '"')
city_country('beijing','China')
	
def make_album(name,album,number=""):
	make_albums = {}
	make_albums['name'] = name
	make_albums['album'] = album
	if number:
		make_albums['number'] = number
	print(make_albums)
	return make_albums
make_album('wo','woo')
make_album('ni','nii')
make_album('ta','taa',90)
print('\n')

while True:
	print("\nPlease enter the message that you have.")
	print("(enter 'q' at any time to quit)")
	
	names = input("Please enter the name: ")
	if names == 'q':
		break
	
	albums = input("Please enter the album: ")
	if albums == 'q':
		break
	
	numbers = input("Please enter the number: ")
	if numbers == 'q':
		break
	
	make_album(names,albums,numbers)
