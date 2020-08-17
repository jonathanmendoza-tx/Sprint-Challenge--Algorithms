'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

	target = 'th'

	count = len(word)

	if count > 1:

		if word[:2] == target:
			return count_th(word[1:]) + 1
		
		return count_th(word[1:])

	else:
		return 0
