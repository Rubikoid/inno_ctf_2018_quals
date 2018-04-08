import random
#import seed
import calendar
import time
enc_numbers = str('tlrKN\\JnZRg\x04bi]WEgOWFoT\x00E')
pref = ''.join([chr(ord(x) ^ ord(y)) for (x, y) in zip(enc_numbers[:4], "CTF{")])
post = ''.join([chr(ord(x) ^ ord(y)) for (x, y) in zip(enc_numbers[-1], "}")])
lec = len(enc_numbers)
print(pref, post)
for i in range(0,626145):
	i = pref + str(i)
	key = (str(i)*lec)[:lec]
	if key[-1] == post:
		data = ''.join([chr(ord(x) ^ ord(y)) for (x, y) in zip(enc_numbers, key)])
		if '|' not in data and '^' not in data and data.count('}') == 1 and data.count('{') == 1:
			print(data)