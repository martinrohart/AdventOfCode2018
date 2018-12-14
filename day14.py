input = 290431

recipes = [3,7]
digits = [int(digit) for digit in str(input)]
elf1 = 0
elf2 = 1
while True:
	recipe1 = recipes[elf1]
	recipe2 = recipes[elf2]
	sum = recipe1 + recipe2
	if(sum>=10):
		r = int(str(sum)[-2])
		r2 = int(str(sum)[-1])
		recipes.extend((r,r2))
	else:
		recipes.extend((sum,))
	elf1 = (elf1+recipe1+1) % len(recipes)
	elf2 = (elf2+recipe2+1) % len(recipes)

	#Part 1
	if len(recipes)==input+10:
		print ''.join(map(str,recipes[-10:]))

	#Part 2
	if recipes[-len(digits):]==digits or recipes[-len(digits)-1:-1]==digits:
		if recipes[-len(digits):] == digits:
			print len(recipes) - len(digits)
		else:
			print len(recipes) - len(digits) - 1
		quit()
