#/usr/bin/python3
# -*- coding: utf-8 -*-
from cursesmenu import *
from cursesmenu.items import *

import requests

import os

fromID = 207
toID = 232
url = 'https://api.hackforces.com/api/task.detail?guid='
url2 = 'https://api.hackforces.com/api/contest.detail?guid=14&token='+\
''
tasks = []

def printTask(id, tasks):
		task = tasks[id]
		print('Title:', task['title'])
		print('Status:', task['status'])
		print('Desc:', task['description'])
		print('Tags:', task['tags'])
		print('Cost:', task['points'])
		print('Category??:', task['category'])
		input()

for i in range(fromID, toID+1):
	tasks.append(requests.get(url+str(i)).json())

for task in tasks:
	if task['title'] == "PPC-300": #fix bad task
		continue
	#old path
	#path = '../' + task['tags'] + str(task['points']) + ' - ' + task['title']	
	#print(task['title'], os.rename(path, new_path))
	path = '../' + task['title']
	#os.rename(path+'/readme.md',path+'/readme.md.back')
	with open(path+'/readme.md', 'w') as f:
		f.write('# '+ task['title'] + "\n\n\n")
		f.write('**Category:** ' + task['tags'] + "\n")
		f.write('**Points:** ' + str(task['points']) + "\n")
		f.write('**Description:**\n\n')
		for i in task['description'].replace('\r', '').split('\n'):
			f.write('> ' + i + '\n')