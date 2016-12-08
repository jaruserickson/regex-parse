#this regex parser is meant for notation used in discrete math.
from random import randint

def recentIndex(list, char, index):
	#returns most recent index of 'char' going back from 'index'
	for i in range(index-1, -1, -1):
		if list[i] == char:
			return i
	return -1

def getIndexes(word, char):
	#returns a list of the indexes of the chars i the wlord
	indexes = []
	for i in range(len(word)):
		if word[i] == char:
			indexes.append(i)
	return indexes

def bracketCheck(outList, chkList, message, i):
	#checks back for recent bracket, and inserts message at appropriate indexes.
	if (chkList[i-1] == ")"):
		outList.insert(recentIndex(chkList, "(", i), message)
	elif(chkList[i-1] == "*"):
		if(chkList[i-2] == ")"):
			outList.insert(recentIndex(chkList, "(", i), message)
		else:
			outList.insert(i-2, message)
	else:
		outList.insert(i-1, message)

def parseEnglish(regex):
	#need to have a getlastindex for the opening bracket when a closing bracket is found
	REGEX_OP = ["(", ")", "+", "*", ".", "?"]

	symbols = []
	out = []

	for x in regex: #adding symbols to a list
		symbols.append(x)

	#need some sort of grammar control here
	for i in range(len(symbols)):
		if symbols[i] == REGEX_OP[0]: #openbracket
			out.append("( ")
		elif symbols[i] == REGEX_OP[1]: #endbracket
			out.append(") ")
		elif symbols[i] == REGEX_OP[2]: #or
			out.append("or ")
		elif symbols[i] == REGEX_OP[3]: #any of
			bracketCheck(out, symbols, "any word of ", i)
		elif symbols[i] == REGEX_OP[4]: #concatenation
			out.append("concatenated with ")
		elif symbols[i] == REGEX_OP[5]: #optionally, not sure
			bracketCheck(out, symbols, "optionally, ", i)
		elif symbols[i].isalpha():
			out.append(symbols[i] + " ")

	return out

def parseExample(regex):
	#create a random example
	#right now only ORs work
	REGEX_OP = ["(", ")", "+", "*", ".", "?"]
	#BEDMAS
	OPEN_BR = getIndexes(regex, "(")
	CLOSE_BR = getIndexes(regex, ")")
	newWord = [] #i need a new word with the evaluated bedmases in here
	outWord = ''
	i = 0

	#evaluate in brackets
	for k in range(len(OPEN_BR)):
		evaluation = evalOr(regex[OPEN_BR[k]+1:CLOSE_BR[k]])
		newWord.append(evaluation)

	#replace bracket values in 'regex'
	for x in range(len(newWord)):
		regex = regex.replace(regex[OPEN_BR[0]:CLOSE_BR[0]+1], newWord[x], 1)
		OPEN_BR = getIndexes(regex, "(")
		CLOSE_BR = getIndexes(regex, ")")

	#need to replace bracket values in regex
	#evaluate out of brackets
	for i in range(len(regex)):
		if regex[i] == "+":
			return evalOr(regex)
		elif regex[i].isalpha():
			outWord = outWord + regex[i]
	return outWord

def evalOr(regex):
	#given some list or string, return the OR of all elements.
	if type(regex) is list:
		random = randint(0, len(regex)-1)
		return regex[random]
	else:
		thisReg = regex.split("+")
		random = randint(0, len(thisReg)-1)
		return thisReg[random]

def concat(list):
	out = ''
	for x in list:
		out += x
	return out

if __name__ == "__main__":
	
	print("/type \'quit\' at any time to exit./")
	print("/type \'next\' for out-type to input another regex./")
	print("REGEX PARSER v0.2")
	#might have lang input + character verification as well

	ENGLISH = ["english", "eng", "e"]
	EXAMPLE = ["example", "ex", "exam"]

	while True: #to simulate a do-while
		regex = input("regex: ")

		if regex == "quit":
			break
		else:
			while True:
				outputType = input("out-type: ")

				if outputType == "next":
					print("---")
					break
				elif outputType == "quit" or outputType == "q":
					break
				elif outputType in ENGLISH:
					print(">>", concat(parseEnglish(regex)))
				elif outputType in EXAMPLE:
					print(">>", parseExample(regex))
				else:
					print("invalid output type.")

			if outputType == "quit":
				break