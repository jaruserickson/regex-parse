#this regex parser is meant for notation used in discrete math.

def parseRegex(regex, outputType):
	REGEX_OPERATORS = ["(", ")", "+", "*", "."];

	symbols = []
	out = []

	for x in regex: #adding symbols to a list
		symbols.append(x)

	if outputType.lower() == "english":

		for i in range(len(symbols)):
			if symbols[i] == REGEX_OPERATORS[0]:
				#openbracket
				out.append("( ")
			elif symbols[i] == REGEX_OPERATORS[1]:
				#endbracket
				out.append(") ")
			elif symbols[i] == REGEX_OPERATORS[2]:
				#or
				out.append("or ")
			elif symbols[i] == REGEX_OPERATORS[3]:
				#any of
				out.insert(symbols.index("("), "any word of ")
			elif symbols[i] == REGEX_OPERATORS[4]:
				#concatenation
				out.append("concatenated with ")
			elif symbols[i].isalpha():
				out.append(symbols[i] + " ")

	elif outputType.lower() == "math":
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