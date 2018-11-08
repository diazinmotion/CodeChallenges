# number of test case
try:
	n = int(input())
except TypeError:
	print("Type is invalid")
	
if n > 0:
	phone_list = {}
	for i in range(n):
		# list untuk phonebook
		new_item = str(input())
		words = new_item.split(' ')

		# push tuple item to phonebook
		phone_list[words[0]] = words[1]


	# search for the name from the phonebook
	# keep read line until EOF (no item remaining)
	search_item = []
	while True:
		try:
			searchable_name = str(input())
			search_item.append(searchable_name)
		except EOFError:
			break

	for i in search_item:
		if i in phone_list:
			print(i + "=" + phone_list[i])
		elif i not in phone_list:
			print("Not found")