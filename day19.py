import re

patternDigit = re.compile(r'.*(\d+)')
patternInstr = re.compile(r'(.{4})\s(\d+)\s(\d+)\s(\d+)')

with open ("input19.txt", "r") as file:
	lines = file.read().strip().split('\n')

rIP = int(patternDigit.match(lines[0]).groups()[0])
data = map(lambda row: (row[0], int(row[1]), int(row[2]), int(row[3])), [patternInstr.match(line).groups() for line in lines[1:]])

def addr(instr, registers):
	registers[instr[3]] = registers[instr[1]] + registers[instr[2]]
	return registers

def addi(instr, registers):
	registers[instr[3]] = registers[instr[1]] + instr[2]
	return registers

def mulr(instr, registers):
	registers[instr[3]] = registers[instr[1]] * registers[instr[2]]
	return registers

def muli(instr, registers):
	registers[instr[3]] = registers[instr[1]] * instr[2]
	return registers

def banr(instr, registers):
	registers[instr[3]] = registers[instr[1]] & registers[instr[2]]
	return registers

def bani(instr, registers):
	registers[instr[3]] = registers[instr[1]] & instr[2]
	return registers

def borr(instr, registers):
	registers[instr[3]] = registers[instr[1]] | registers[instr[2]]
	return registers

def bori(instr, registers):
	registers[instr[3]] = registers[instr[1]] | instr[2]
	return registers

def setr(instr, registers):
	registers[instr[3]] = registers[instr[1]]
	return registers

def seti(instr, registers):
	registers[instr[3]] = instr[1]
	return registers

def gtir(instr, registers):
	if instr[1]>registers[instr[2]]:
		registers[instr[3]] = 1
	else:
		registers[instr[3]] = 0
	return registers

def gtri(instr, registers):
	if registers[instr[1]]>instr[2]:
		registers[instr[3]] = 1
	else:
		registers[instr[3]] = 0
	return registers

def gtrr(instr, registers):
	if registers[instr[1]]>registers[instr[2]]:
		registers[instr[3]] = 1
	else:
		registers[instr[3]] = 0
	return registers

def eqir(instr, registers):
	if instr[1]==registers[instr[2]]:
		registers[instr[3]] = 1
	else:
		registers[instr[3]] = 0
	return registers

def eqri(instr, registers):
	if registers[instr[1]]==instr[2]:
		registers[instr[3]] = 1
	else:
		registers[instr[3]] = 0
	return registers

def eqrr(instr, registers):
	if registers[instr[1]]==registers[instr[2]]:
		registers[instr[3]] = 1
	else:
		registers[instr[3]] = 0
	return registers

def runInstr(instr, registers):
	operation = instr[0]
	if operation=='addr':
		registers = addr(instr,registers)
	elif operation=='addi':
		registers = addi(instr,registers)
	elif operation=='mulr':
		registers = mulr(instr,registers)
	elif operation=='muli':
		registers = muli(instr,registers)
	elif operation=='banr':
		registers = banr(instr,registers)
	elif operation=='bani':
		registers = bani(instr,registers)
	elif operation=='borr':
		registers = borr(instr,registers)
	elif operation=='bori':
		registers = bori(instr,registers)
	elif operation=='setr':
		registers = setr(instr,registers)
	elif operation=='seti':
		registers = seti(instr,registers)
	elif operation=='gtir':
		registers = gtir(instr,registers)
	elif operation=='gtri':
		registers = gtri(instr,registers)
	elif operation=='gtrr':
		registers = gtrr(instr,registers)
	elif operation=='eqir':
		registers = eqir(instr,registers)
	elif operation=='eqri':
		registers = eqri(instr,registers)
	elif operation=='eqrr':
		registers = eqrr(instr,registers)
	registers[rIP] += 1 
	return registers

#Part1
registers = [0 for i in range(6)]
while registers[rIP]<len(data):
	registers = runInstr(data[registers[rIP]], registers)
print registers

#Part 2
registers = [1,0,0,0,0,0]
hitmap = [0 for i in data]
while registers[rIP]<len(data):
	#hitmap[registers[rIP]] += 1
	#print hitmap
	#the hitmap tells us all time spent in instructions 3-6, 8-11

	#mulr 4 5 1 -> register 1 = register 4 * register 5
	#eqrr 1 3 1 -> (register 1 == register 3) ? register 1 <- 1 : register 1 <- 0
	#addr 1 2 2 -> IP = IP + register 1
	#addi 2 1 2 -> IP = IP + 1 i.e. skip next line
	#Skipped until r5 reaches r3 -> register 0 += register4 *I.e. add the divisor of r3
	#addi 5 1 5 -> register 5 = register 5 + 1
	#gtrr 5 3 1 -> (register 5 > register 3) ? register 1 <- 1 : register 1 <- 0
	#addr 2 1 2 -> IP = IP + register 1
	#seti 2 6 2 -> IP = 2 i.e next instruction will be the first in this list

	# loop 3-6: comes with r5=1, until r4 exactly r3 initial (10551374), we loop, when reached, r0 increments with 10551374
	# register 0 = untouched
	# register 1 = 1 
	# register 2 = IP = 7
	# register 3 = untouched (10551374)
	# register 4 = 10551374
	# register 5 = 1 

	# loop 8-11: so until r5 is more than r3 initial (10551374), we loop, when reached, we skip to line after this loop, with r5 = r3+1
	# register 0 = untouched
	# register 1 = 1
	# register 2 = IP = 12
	# register 3 = untouched
	# register 4 = untouched
	# register 5 = r3+1

	# loop 12-16:
	# addi 4 1 4: r4++
	# gtrr 4 3 1 -> (register 4 > register 3) ? register 1 <- 1 : register 1 <- 0
	# addr 1 2 2 -> IP = IP + register 1
	# seti 1 7 2 -> go to 2
	# mulr 2 2 2 -> IP = IP*IP=16*16: out of stack

	if registers[rIP]==3:
		x = registers[3]
		for i in range(1, x+1):
			if x % i == 0:
				registers[0] += i
		registers = [registers[0], 1, 12, registers[3], registers[3], registers[3]+1]
	else:
		registers = runInstr(data[registers[rIP]], registers)
print registers
