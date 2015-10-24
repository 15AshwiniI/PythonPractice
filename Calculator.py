#this is how you comment in python
print "Welcome to Calculator!"

print "Enter your first number"
a = input()

print "Enter your second number"
b = input()

print "What calculation whould you like to do?"
print "Addition, Subtraction, Multiplication, Division"
p = raw_input()

if p == "Addition":
    print "Answer: "+ str(a + b)

elif p == "Subtraction":
    print "Answer: "+ str(a - b)

elif p == "Multiplication":
    print "Answer: "+ str(a * b)

elif p == "Division":
    print "Answer: "+ str(a / b)

else:
    print "Not a valid calculation"

print "goodbye!"
