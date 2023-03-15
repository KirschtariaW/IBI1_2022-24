# What does this piece of code do?
# Answer:from a loop for 10 times, pick the biggest number we get in 10 random numbers


# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

#to get a start value
progress=0
stored_random_number=0
while progress<10:
	progress+=1 #means: progress=progress+1
	n = randint(1,100)#pick a randint from 1 to 100
	if n > stored_random_number:
		stored_random_number = n
#if n > stored_random_number, store the n as the new number;if not, dom't save and start a new loop

print(stored_random_number)
