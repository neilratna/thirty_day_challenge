# Exercises for chapter 3: Problems 3.1, 3.2, 3.3, and 3.4 in Think Python

# Neil Ratna

#3.1 & 3.2
import math

#def repeat_lyrics():
#	print_lyrics()
#	print_lyrics()

#def print_lyrics():
#	print "I'm a lumberjack, and I'm okay."
#	print "I sleep all night and I work all day"

#repeat_lyrics()

#3.1 get a NameError that repeat_lyrics is not defined
#3.2 this program runs ok

#3.3

#def right_justify(s):
#	print (''*(70-len(s))+s)

#right_justify('allen')

#3.4

def do_twice(f):
	f()
	f()

def print_spam():
	print 'spam'

do_twice(print_spam)

#1. displays spam twice

