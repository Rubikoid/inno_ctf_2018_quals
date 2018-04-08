#/usr/bin/python3
# -*- coding: utf-8 -*-
from cursesmenu import *
from cursesmenu.items import *

import requests

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

solved = []
for i in requests.get(url2).json()['tasks']:
	if i['solved'] == True:
		solved.append(i['title'])

tList = [i['title'] if i['title'] not in solved else '\/ '+i['title'] for i in tasks]

#if u need tasks in file
"""
with open('tas.txt', 'w') as f:
	for task in tasks:
		f.write("Name: "+task['title'])
		f.write("\nDesc: "+task['description'])
		f.write('\nCost: '+str(task['points']))
		f.write('\nTags: '+task['tags'])
		f.write('\n\n')
"""

while True:
	selected = SelectionMenu.get_selection(tList)
	if selected == len(tList):
		break
	printTask(selected, tasks)