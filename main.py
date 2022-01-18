import requests
from bs4 import BeautifulSoup

input_path = 'input.txt'
output_text_list = []

with open(input_path, 'r') as f:
	file_data = f.readlines()
	for link in file_data:
		link = link.rstrip()
		r = requests.get(link)
		soup = BeautifulSoup(r.text)
		output_text_list.append(soup.find("title").text + '|' + link)

with open('output.txt', 'w') as f:
	f.write('\n'.join(output_text_list))
