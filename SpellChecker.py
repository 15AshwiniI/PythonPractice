# used tutorial on: http://www.openbookproject.net/py4fun/spellCheck/index.html
print "Welcome to SpellChecker"

#opens and reads from the spell.words file. It has over 50,000 words and serves as our dictionary
words = open("spell.words.txt").readlines()

#The strip function is needed to remove the newline character at the end of each word.
words = map(lambda x: x.strip(), words)
print "a" in words
for i in range(1000) : a = 'zygotic' in words
print "completed"

test = open("Words.txt").readlines()
#test = map(lambda y: y.strip(), test)
test = test[0].split()
print "cat is in words?"
print "cat" in words
print test[1]

