#!/bin/python
import json
import os
import requests
import shutil

ending = "2022_12_28.txt" # CHANGE THIS TO THE LATEST DATE OF RELEASE

url = "https://wordlists-cdn.assetnote.io/data/"
assetnote = ["automated", "manual", "technologies", "kiterunner"]

c = "s"
while not (c == "y" or c == "n"):
	c = input("Do you want to remove 'httparchive_' and from the name of the wordlist?: (Y/N)").lower()

if not os.path.exists("./assetnote"):
    os.makedirs("./assetnote")
if not os.path.exists("./assetnote/temp"):
    os.makedirs("./assetnote/temp")

for i in range(len(assetnote)):
	temp_url = url + assetnote[i] + ".json"
	r = requests.get(temp_url)
	with open("./assetnote/temp/" + assetnote[i] + ".json", 'wb') as f:
		f.write(r.content) 
		f.close()

for j in range(len(assetnote)):
	with open("./assetnote/temp/" + assetnote[j] + ".json", mode='r') as read_file:
		object = json.load(read_file)
		for i in object['data']:
			os.system('cls||clear')
			if i['Filename'].endswith(ending):
				print("DOWNLOADING - {} [Size: {}]".format(i['Filename'],i['File Size']))
				temp_url = url + assetnote[j] + "/" + i['Filename']
				r = requests.get(temp_url)
				with open("./assetnote/" + i['Filename'], 'wb') as f:
					f.write(r.content) 
					f.close()

shutil.rmtree("./assetnote/temp/")

dir_list = os.listdir("./assetnote/")
for x in range(len(dir_list)):
	if os.stat("./assetnote/" + dir_list[x]).st_size == 0:
		os.remove("./assetnote/" + dir_list[x])
		print("EMPTY FILE DELETED: {}".format(dir_list[x]))

if c == "y":
	dir_list = os.listdir("./assetnote/")
	for x in range(len(dir_list)):
		os.rename("./assetnote/" + dir_list[x], "./assetnote/" + dir_list[x][12:])
print("DONE")
