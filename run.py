#run this file to run the parser

import discrete_regex, lang_regex

if __name__ == "__main__":
	print("/type \'quit\' at any time to exit./")

	invalid = False

	while True:
		DISCRETE = ['d', 'discrete', 'lazy', 'greedy']
		LANG = ['l', 'lang', 'java', 'python', 'javascript', 'perl', 'js', 'py']
		QUIT = ['q', 'quit']

		if not invalid:
			print("/type discrete (d) or lang (l) to choose regex type./")
			print("REGEX PARSER")

		stdin = input("regex-type: ")

		if stdin.lower() in DISCRETE:
			print("----------")
			discrete_regex.runDisc()
			print("back to main...")
			print("----------")
			invalid = False
		elif stdin.lower() in LANG:
			print("----------")
			lang_regex.runLang()
			print("back to main...")
			print("----------")
			invalid = False
		elif stdin.lower() in QUIT:
			break
		else:
			print("invalid type.")
			invalid = True