#this regex parser is meant for notation used in discrete math.

def parseRegex(regex, outputType):
	#need to have a getlastindex for the opening bracket when a closing bracket is found
	REGEX_OP = ["(", ")", "+", "*", ".", "?"]
	ENGLISH = ["english", "eng", "e"]
	MATH = ["math", "m", "symbols", "sym"]

	symbols = []
	out = []

	for x in regex: #adding symbols to a list
		symbols.append(x)

	if outputType.lower() in ENGLISH:
		#need some sort of grammar control here
		for i in range(len(symbols)):
			if symbols[i] == REGEX_OP[0]:
				#openbracket
				out.append("( ")
			elif symbols[i] == REGEX_OP[1]:
				#endbracket
				out.append(") ")
			elif symbols[i] == REGEX_OP[2]:
				#or
				out.append("or ")
			elif symbols[i] == REGEX_OP[3]:
				#any of
				out.insert(symbols.index("("), "any word of ")
			elif symbols[i] == REGEX_OP[4]:
				#concatenation
				out.append("concatenated with ")
			elif symbols[i] == REGEX_OP[5]:
				#optionally
				if (symbols[i-1] == REGEX_OP[1]):
					out.insert(symbols.index("("), "optionally, ")
				elif(symbols[i-1] == REGEX_OP[3]):
					if(symbols[i-2] == REGEX_OP[1]):
						out.insert(symbols.index("("), "optionally, ")
					else:
						out.insert(i-2, "optionally, ")
				else:
					out.insert(i-1, "optionally, ")
			elif symbols[i].isalpha():
				out.append(symbols[i] + " ")

	elif outputType.lower() in MATH:
		print("maf")
	else:
		print("invalid output type.")

	return out

def concat(list):
	out = ''
	for x in list:
		out += x
	return out

if __name__ == "__main__":
	print("REGEX PARSER v0.1")
	#add quit at any point
	#add move on so user can do multiple output types
	print(concat(parseRegex(input("regex: "), input("output type: "))))