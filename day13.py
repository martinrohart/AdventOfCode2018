from operator import itemgetter

with open ("input13.txt", "r") as file:
	lines = map(lambda l: list(l), file.read().split('\n'))

moves = { 
			('/','v'): '<',
		 	('/','^'): '>',
		 	('/','>'): '^',
		 	('/','<'): 'v',
		 	('\\','v'): '>',
		 	('\\','^'): '<',
		 	('\\','>'): 'v',
		 	('\\','<'): '^',
		 	('+','v',0): '>',
		 	('+','^',0): '<',
		 	('+','>',0): '^',
		 	('+','<',0): 'v',
		 	('+','v',2): '<',
		 	('+','^',2): '>',
		 	('+','>',2): 'v',
		 	('+','<',2): '^'
		}

carts = []
for y in range(len(lines)):
	for x in range(len(lines[y])):
		c = lines[y][x]
		if c=='v' or c=='^' or c=='>' or c=='<':
			carts.append([x,y,c,0])
		if c=='v' or c=='^':
			lines[y][x] = '|'
		elif c=='>' or c=='<':
			lines[y][x] = '-'

while len(carts)>1:
	carts = sorted(carts, key=itemgetter(1,0))
	crashed = []
	for c in range(len(carts)):
		if c in crashed:
			continue
		cart = carts[c]

		#Update coordinates
		if cart[2]=='v':
			cart[1]+=1
		elif cart[2]=='^':
			cart[1]-=1
		elif cart[2]=='>':
			cart[0]+=1
		elif cart[2]=='<':
			cart[0]-=1

		#Update direction
		direction = lines[cart[1]][cart[0]]
		if (direction, cart[2]) in moves:
			cart[2] = moves[(direction, cart[2])]
		elif (direction, cart[2], cart[3]) in moves:
			cart[2] = moves[(direction, cart[2], cart[3])]
			
		#Update crossing status
		if direction == '+':
			cart[3] = (cart[3] + 1) % 3

		#Check crashes
		for c2 in range(len(carts)):
			if c2!=c:
				if carts[c2][0]==carts[c][0] and carts[c2][1]==carts[c][1]:
					print "Collision at %s,%s" % (carts[c][0], carts[c][1])
					crashed.append(c)
					crashed.append(c2)
	if crashed:
		carts = [carts[i] for i in range(len(carts)) if not i in crashed]

print "Last cart at %s,%s" % (carts[0][0], carts[0][1])