#perl-style (i.e java, javascript, python)

#checklist
#^  yes
#$  yes
#+  no
#*  no
#() yes
#[] no
#[other] ??
#^, (), *, +, $, (abasd), [asbdasd], [a-zA-Z0-9], [a-zA-Z], [0-9] and more

import random
from random import randint
from discrete_regex import concat, recentIndex, getIndexes, bracketCheck

def evalParens(regex, lower, upper): #(OR)
	orString = ""
	for x in regex[lower, upper]:
		if x != regex[upper - 1]:
			orString += x + " or "
		else:
			orString += x
	return orString

def parseEnglish(regex):
	#(str) -> (list of str)
	#^(abc).*(abc)$
	# starts and ends with a or b or c with any contents
	output, symbols = [], []
	OPEN_BR = getIndexes(regex, "(")
	CLOSE_BR = getIndexes(regex, ")")
	for x in regex:
		symbols.append(x)

	cursor = 0 				#cursor for loop
	bpoint = len(regex) - 1 #breakpoint for end of loop
	if symbols[0] == "^":
		if symbols[1] == "(":
			output.append("starts with " + evalParens(regex, OPEN_BR[0] + 1, \
														CLOSE_BR[0]) + " ")
			cursor = CLOSE_BR[0] + 1
		else:
			output.append("starts with " + regex[1] + " ")
			cursor = 2

	if symbols[len(symbols) - 1] == "$":
		if symbols[len(symbols) - 2] == ")":
			output.append("ends with " + evalParens(regex, \
			  OPEN_BR(len[OPEN_BR) - 1] + 1, CLOSE_BR[len(CLOSE_BR) - 1]) + " ")

			bpoint = OPEN_BR[len(OPEN_BR) - 2] #break after equal this
		else:
			out.put.append("ends with " + regex[len(regex) - 2] + " ")
			bpoint = len(regex) - 3


	while cursor != bpoint + 1
		#bulk of parsing happens here


	return output

def parseExample(regex):
	#(str) -> (str)
	print("not implemented.")

def runLang():
	print("/type \'next\' for out-type to input another regex./")
	print("/choose example (ex) or english (e) for out-type./")
	print("perl v0.01")

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

if __name__ == "__main__":
	print("/type \'quit\' at any time to exit./")
	runLang()
