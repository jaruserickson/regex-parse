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
	REGEX_OP = ["(", ")", "+", "*", ".", "?"]
	#BEDMAS
	OPEN_BR = getIndexes(regex, "(")
	CLOSE_BR = getIndexes(regex, ")")
	newWord = "" #i need a new word with the evaluated bedmases in here
	i = 0
	#now that we have matching open/close brackets, assuming user input is proper
	#we can evaluate from bracket to bracket with another function.
	while i < len(regex):
		if i in OPEN_BR:
			newWord = newWord + evalOr(regex[OPEN_BR[i]+1:CLOSE_BR[i]])
			i = CLOSE_BR[i]+1
		elif regex[i] == "+":
			return evalOr(regex)
		else:
			newWord = newWord + regex[i]
			i = i + 1
	return newWord

def evalOr(regex):
	pieces = regex.split("+")
	random = randint(0, len(pieces)-1)
	return pieces[random]

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
				elif outputType == "quit":
					break
				elif outputType in ENGLISH:
					print(">>", concat(parseEnglish(regex)))
				elif outputType in EXAMPLE:
					print(">>", parseExample(regex))
				else:
					print("invalid output type.")

			if outputType == "quit":
				break