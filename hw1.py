"""
Homework 1 
CIS4930
Summer 17
Ryan Winter
rw15e
"""

from __future__ import print_function
import enchant 
import random
d = enchant.Dict("en_US")

diceLayout = [
	['A', 'E', 'A', 'N', 'E', 'G'],   
	['A', 'H', 'S', 'P', 'C', 'O'],
	['A', 'S', 'P', 'F', 'F', 'K'], 
	['O', 'B', 'J', 'O', 'A', 'B'], 
	['I', 'O', 'T', 'M', 'U', 'C'], 
	['R', 'Y', 'V', 'D', 'E', 'L'],  
	['L', 'R', 'E', 'I', 'X', 'D'],  
	['E', 'I', 'U', 'N', 'E', 'S'],  
	['W', 'N', 'G', 'E', 'E', 'H'],
	['L', 'N', 'H', 'N', 'R', 'Z'],    
	['T', 'S', 'T', 'I', 'Y', 'D'],   
	['O', 'W', 'T', 'O', 'A', 'T'],   
	['E', 'R', 'T', 'T', 'Y', 'L'],
	['T', 'O', 'E', 'S', 'S', 'I'],   
	['T', 'E', 'R', 'W', 'H', 'V'],
	['N', 'U', 'I', 'H', 'M', 'Qu']
]

randList = [] # this holds the random dice roll values
currList = [] # this holds the current 16 values chosen by dice

for j in range(16):
	rand1 = random.randint(0, 5)
	randList.append(rand1)
	if(j<4):
		print("[", diceLayout[j][rand1], "] ", "[", diceLayout[j+1][rand1], "] ", "[", diceLayout[j+2][rand1], "] ", "[", diceLayout[j+3][rand1], "]", sep='', end='\n')
		print("")
		currList.append(diceLayout[j][rand1])
		currList.append(diceLayout[j+1][rand1])
		currList.append(diceLayout[j+2][rand1])
		currList.append(diceLayout[j+3][rand1])
		



"""diceLayout is name of item holding all dice possibilities"""



print("Start typing your words! (press enter after each word and enter 'X' when done): ")
myList = []
count = 0
breakVar = 0
totalScore = 0

while(breakVar != 5):
	x = raw_input()
	myList.append(x.upper())
	count = count + 1
	if(x.upper() == 'X'):
		breakVar = 5 
	

for i in xrange(count-1):
	""" check if already scored, if too short, if is a word, if its present in grid, if it uses same letter cube more than once"""
	if (len(myList[i]) < 3 ):
		print("The word",myList[i], "is too short.")
	elif (d.check(myList[i]) == False):
		print("The word",myList[i], "is not a word.")
	elif (len(myList[i]) == 3):
		print("The word",myList[i], "is worth 1 point.")
		totalScore += 1
	elif (len(myList[i]) == 4):
		print("The word",myList[i], "is worth 1 point.")
		totalScore += 1
	elif (len(myList[i]) == 5):
		print("The word",myList[i], "is worth 2 points.")
		totalScore += 2
	elif (len(myList[i]) == 6):
		print("The word",myList[i], "is worth 3 points.")
		totalScore += 3
	elif (len(myList[i]) == 7):
		print("The word",myList[i], "is worth 5 points.")
		totalScore += 5
	elif (len(myList[i]) >= 8):
		print("The word",myList[i], "is worth 11 points.")
		totalScore += 11

print("Your total score is",totalScore,"points!")



def searchForWord():
	# this will search for the given word inside the board
	# need to test inside for loop over whole board, inner for loop through the full word. if 		# word[i] = myList[j] then implement list of if statements checking the proper surrounding 
	# places
	for k in xrange(15):
		tempWord = myList[k]
		tempBoardWord = currList[k]
		matchFound = False
		while(matchFound == False):
			if(tempWord[0] == tempBoardWord[k]): # test first letter through whole board
				matchFound = True
		
		
		#for l in xrange(count-1):
			
				# if both match, continue searching until not found.
				

	return

