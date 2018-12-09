#input:
#452 players; last marble is worth 70784 points
from collections import deque

def playFast(players, lastMarble):

	circle = deque([0]) 
	currentPlayer = 0
	scores = [0 for i in range(players)]

	for marble in range(1,lastMarble+1):
		if marble % 23==0:
			circle.rotate(7)
			scores[currentPlayer] += marble + circle.popleft()
		else:
			circle.rotate(-2)
			circle.extendleft([marble])
		#print "Circle: %s" % (circle)

		currentPlayer +=1
		if currentPlayer>=players:
			currentPlayer = 0

	return max(scores)

def play(players, lastMarble):

	circle = [0]
	current = 0
	currentPlayer = 0
	scores = [0 for i in range(players)]

	for marble in range(1,lastMarble+1):
		#print "Marble: %s by player %s" % (marble, currentPlayer)
		if marble % 23==0:
			score = marble	
			current = current - 7
			if current<0:
				current = len(circle)+current
			score += circle[current]
			circle = circle[0:current] + circle[current+1:]
			scores[currentPlayer] += score

		else:
			current = ((current+2) % len(circle)) 
			circle = circle[0:current] + [marble] + circle[current:]
		#print "Circle: %s - current is %s" % (circle, str(circle[current]))

		currentPlayer +=1
		if currentPlayer>=players:
			currentPlayer = 0

	return max(scores)

#print play(452, 70784)
print playFast(452, 70784)

# Part 2
print playFast(452, 100*70784)
