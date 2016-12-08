#this regex parser is meant for notation used in discrete math.
from random import randint

def recentIndex(list, char, index):
	#returns most recent index of 'char' going back from 'index'
	for i in range(index-1, -1, -1):
		if list[i] == char:
			return i
	return -1

def nextIndex(list, char, index):
	#return next index of 'char' going forwards from index
	for i in range(index, len(list)):
		if list[i] == char:
			return i

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

def parseRegex(regex, outputType):
	#need to have a getlastindex for the opening bracket when a closing bracket is found
	REGEX_OP = ["(", ")", "+", "*", ".", "?"]

	symbols = []
	out = []

	for x in regex: #adding symbols to a list
		symbols.append(x)

	if outputType.lower() in ENGLISH:
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
	#create an example.
	REGEX_OP = ["(", ")", "+", "*", ".", "?"]

	symbols = []
	out = []
	i = 0	

	for x in regex: #adding symbols to a list
		symbols.append(x)
	#out what we're using to bring operations together here
	ex = randint(1,5) #example context
	while i < len(symbols):
		if symbols[i] == REGEX_OP[0]: #openbracket
		#operate on stuff inside bracket until endbracket
			thisExample = []
			farIndex = nextIndex(symbols, ")", i)
			for x in range(i+1, farIndex):
				thisExample.append(symbols[x])
			i = farIndex
			parseExample(thisExample)	

		elif symbols[i] == REGEX_OP[2]: #or
			#or the two operands
			if ex%2 != 0:
				out.append(out[0:i])
			else:
				out.append(out[i:len(out)-1])
			i = i + 1
		elif symbols[i] == REGEX_OP[3]: #any of
			#choose some concatenation of the contents
			out.append(out[i-1]*ex)
			i = i + 1
		elif symbols[i] == REGEX_OP[4]: #concatenation
			#combine the two terms???
			print("lol")
			i = i + 1
		elif symbols[i] == REGEX_OP[5]: #optionally, not sure
			#randomly 1 or 0, choose to include or not
			if ex%2 == 0:
				out.append(out[i-1])
			i = i + 1
		elif symbols[i].isalpha():
			out.append(symbols[i])
			i = i + 1

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
					print(">>", concat(parseExample(regex)))
				else:
					print("invalid output type.")

			if outputType == "quit":
				break