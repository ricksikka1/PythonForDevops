file_path = 'sample3.txt'

with open(file_path, 'r') as open_file:
	text = open_file.readlines()
	print(text[15])

new_text = '''export STAGE=PROD
export TABLE_ID=token-storage-1234'''

with open('.envrc', 'w') as opened_file:
	opened_file.write(new_text)
