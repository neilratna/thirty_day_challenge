# Exercises for chapter 2: Problems 2.1, 2.2, 2.3, and 2.4 in Think Python

# Neil Ratna

#2.1
# python thinks you want to convert from an octal number to a decimal number. Zipcode 02492 is invalid because 9 is not a valid octal number. 

#2.2

5
x = 5
x + 1
print x
output is 5

print 5
print x = 5
print X + 1

# this will show exactly what i just typed out

#2.3

width = 17
height = 12.0
delimiter = '.'

print width/2 #displays 8
print width/2.0 #displays 8.5
print height/3 #displays 4.0
print 1 + 2 * 5 #displays 11
print delimiter * 5 #displays .....

#2.4 #1

pi = 3.14159
r = 5.0
volume = 4.0/3.0 * pi * r ** 3
print volume #displays 523.59833333

#2.4 #2

wholesale = 24.95 * 0.6 * 60 + 0.75 * (60-1) +3
print wholesale #displays 945.45

#2.4 #3

start = (6*60+52) * 60
easy = (8*60+15) * 2
tempo = (7*60+12) *3
finish_hour = (start + easy +tempo)/(60*60.0)
finish_floor = (start + easy + tempo)/(60*60)
finish_min = (finish_hour - finish_floor)*60
print 'Home for breakfast at %d:%d' % (finish_hour,finish_min)
#displays 7:30




