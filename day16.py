import re

pattern = re.compile(r'(\d+)')

with open ("input16-1.txt", "r") as file:
	lines = file.read().strip().split('\n')

before = []
instruction = []
after = []
index=0
for l in lines:
	data = map(int,re.findall(pattern, l))
	if data:
		if index % 3==0:
			before.append(data)
		elif index % 3==1:
			instruction.append(data)
		elif index % 3==2:
			after.append(data)
		index+=1

def initRegisters(before):
	return [before[0],before[1], before[2], before[3]]


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


def getMatches(instr, before, after):
	matches = []
	if after == addr(instr, initRegisters(before)):
		matches.append('addr')
	if after == addi(instr, initRegisters(before)):
		matches.append('addi')
	if after == mulr(instr, initRegisters(before)):
		matches.append('mulr')
	if after == muli(instr, initRegisters(before)):
		matches.append('muli')
	if after == banr(instr, initRegisters(before)):
		matches.append('banr')
	if after == bani(instr, initRegisters(before)):
		matches.append('bani')
	if after == borr(instr, initRegisters(before)):
		matches.append('borr')
	if after == bori(instr, initRegisters(before)):
		matches.append('bori')
	if after == setr(instr, initRegisters(before)):
		matches.append('setr')
	if after == seti(instr, initRegisters(before)):
		matches.append('seti')
	if after == gtir(instr, initRegisters(before)):
		matches.append('gtir')
	if after == gtri(instr, initRegisters(before)):
		matches.append('gtri')
	if after == gtrr(instr, initRegisters(before)):
		matches.append('gtrr')
	if after == eqir(instr, initRegisters(before)):
		matches.append('eqir')
	if after == eqri(instr, initRegisters(before)):
		matches.append('eqri')
	if after == eqrr(instr, initRegisters(before)):
		matches.append('eqrr')
	return matches

matches = []
for i in range(len(instruction)):
	matches.append(getMatches(instruction[i],before[i],after[i]))
print len(filter(lambda m: m>=3,map(lambda m: len(m), matches)))

#Part 2
operations = {}

while len(operations.keys())<16:
	filtered = filter(lambda m: len(m)==1, matches)
	for m in range(len(matches)):
		if len(matches[m])==1:
			operations[instruction[m][0]] = matches[m][0]
			matches[m] = []

	def cleanKnownOperations(m):
		m = filter(lambda v: v not in operations.values(),m)
		return m

	matches = map(cleanKnownOperations, matches)

print operations
with open ("input16-2.txt", "r") as file:
	data = map(lambda l: map(int, re.findall(pattern, l)), file.read().strip().split('\n'))

registers = initRegisters([0,0,0,0])
for instr in data:
	operation = operations[instr[0]]
	if operation=='addr':
		registers = addr(instr,registers)
	if operation=='addi':
		registers = addi(instr,registers)
	if operation=='mulr':
		registers = mulr(instr,registers)
	if operation=='muli':
		registers = muli(instr,registers)
	if operation=='banr':
		registers = banr(instr,registers)
	if operation=='bani':
		registers = bani(instr,registers)
	if operation=='borr':
		registers = borr(instr,registers)
	if operation=='bori':
		registers = bori(instr,registers)
	if operation=='setr':
		registers = setr(instr,registers)
	if operation=='seti':
		registers = seti(instr,registers)
	if operation=='gtir':
		registers = gtir(instr,registers)
	if operation=='gtri':
		registers = gtri(instr,registers)
	if operation=='gtrr':
		registers = gtrr(instr,registers)
	if operation=='eqir':
		registers = eqir(instr,registers)
	if operation=='eqri':
		registers = eqri(instr,registers)
	if operation=='eqrr':
		registers = eqrr(instr,registers)
print registers