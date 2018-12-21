from assembly import *

rIP, data = initProgram("input21.txt")

def run(registers):
	#seti 123 0 3 -> r3=123
	#bani 3 456 3 ->  r3 = r3 & 456 = 123&456 then 0 & 456
	#eqri 3 72 3  -> r3=1 if r3=72 so r3 = 1 if (123 & 456 = 72)
	#addr 3 5 5 -> IP = IP+r3 = 3+ (1 or 0) 
	#seti 0 0 5 -> IP = 0: i.e. go to bani
	#seti 0 0 3 -> Passed binary test: IP =5

	# Line 28 is first time r0 used:
	# eqrr 3 0 1
	# Check r3 on line 28: when equal, it exits, else loops back to IP=6

	cnt=0
	while registers[rIP]<len(data) and cnt<10000:
		registers = runInstr(data[registers[rIP]], registers, rIP)
		if registers[rIP]==28:
			print "we need %s" % registers[3]
			return registers[3]
		cnt+=1
	return False

def run2(registers):
	seen = {}
	last = 0
	while registers[rIP]<len(data):
		registers = runInstr(data[registers[rIP]], registers, rIP)
		if registers[rIP]==28:
			print registers[3]
			if registers[3] in seen:
				print "Repeating here, longest run is %s" % last
				return True
			last = registers[3]
			seen[registers[3]] = True
	return False

run([0,0,0,0,0,0])
run2([0,0,0,0,0,0])
