#Assembly code lib
import re

def initProgram(inputFile):
	patternDigit = re.compile(r'.*(\d+)')
	patternInstr = re.compile(r'(.{4})\s(\d+)\s(\d+)\s(\d+)')

	with open (inputFile, "r") as file:
		lines = file.read().strip().split('\n')

	rIP = int(patternDigit.match(lines[0]).groups()[0])
	data = map(lambda row: (row[0], int(row[1]), int(row[2]), int(row[3])), [patternInstr.match(line).groups() for line in lines[1:]])
	return rIP, data

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

def runInstr(instr, registers, rIP):
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