#!/bin/python
import json
import os
import requests
import shutil

ending = "2022_12_28.txt" # CHANGE THIS TO THE LATEST DATE OF RELEASE

url = "https://wordlists-cdn.assetnote.io/data/"
assetnote = ["automated", "manual", "technologies", "kiterunner"]

if not os.path.exists("./assetnote_wordlists"):
    os.makedirs("./assetnote_wordlists")
if not os.path.exists("./assetnote_wordlists/temp"):
    os.makedirs("./assetnote_wordlists/temp")

for i in range(len(assetnote)):
	temp_url = url + assetnote[i] + ".json"
	r = requests.get(temp_url)
	with open("./assetnote_wordlists/temp/" + assetnote[i] + ".json", 'wb') as f:
		f.write(r.content) 
		f.close()

c = "s"
while not (c == "y" or c == "n"):
	c = input("Do you want to remove 'httparchive_' and from the name of the wordlist?: (Y/N)").lower()

if c == "y":
	for j in range(len(assetnote)):
		with open("./assetnote_wordlists/temp/" + assetnote[j] + ".json", mode='r') as read_file:
			object = json.load(read_file)
			for i in object['data']:
				os.system('cls||clear')
				if i['Filename'].endswith(ending):
					print("DOWNLOADING - {} [Size: {}]".format(i['Filename'][12:],i['File Size']))
					temp_url = url + assetnote[j] + "/" + i['Filename'][12:]
					r = requests.get(temp_url)
					with open("./assetnote_wordlists/" + i['Filename'][12:], 'wb') as f:
						f.write(r.content) 
						f.close()

else:
	for j in range(len(assetnote)):
		with open("./assetnote_wordlists/temp/" + assetnote[j] + ".json", mode='r') as read_file:
			object = json.load(read_file)
			for i in object['data']:
				os.system('cls||clear')
				if i['Filename'].endswith(ending):
					print("DOWNLOADING - {} [Size: {}]".format(i['Filename'],i['File Size']))
					temp_url = url + assetnote[j] + "/" + i['Filename']
					r = requests.get(temp_url)
					with open("./assetnote_wordlists/" + i['Filename'], 'wb') as f:
						f.write(r.content) 
						f.close()

shutil.rmtree("./assetnote_wordlists/temp/")

print("DONE")
