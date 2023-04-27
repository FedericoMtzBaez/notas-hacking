f = open('message.txt').read().split()

flag = ''

for n in f:
	n= int(n) % 37
	if n>=0 and n<=25:
		c = chr(n+65)
	elif n>=26 and n<=35:
		c = chr(n+22)
	else : c='_'

	flag += c


print(flag)
	
