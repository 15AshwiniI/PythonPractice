# used tutorial on: http://www.openbookproject.net/py4fun/spellCheck/index.html
print "Welcome to SpellChecker"

#opens and reads from the spell.words file. It has over 50,000 words and serves as our dictionary
words = open("spell.words.txt").readlines()

#The strip function is needed to remove the newline character at the end of each word.
words = map(lambda x: x.strip(), words)

test = open("Words.txt").readlines()
print test
test = test[0].split()

counter = 0;
for t in range(0,len(test)):
    if test[t] in words:
    	t + 1
    else:
    	print test[t] + " is not a word"
    	counter = counter + 1

if counter is 0:
	print "There were no spelling errors in this file"

