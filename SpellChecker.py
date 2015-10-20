# used tutorial on: http://www.openbookproject.net/py4fun/spellCheck/index.html
print "Welcome to SpellChecker"

#opens and reads from the spell.words file. It has over 50,000 words and serves as our dictionary
words = open("spell.words.txt").readlines()
words = map(lambda x: x.strip(), words)
print "a" in words
for i in range(1000) : a = 'zygotic' in words
print "completed"