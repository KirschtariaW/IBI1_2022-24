#start with 2 rabbits,generation=1
n=2
generation=1
print(generation,n)
#the number of rabbits=2n
#a loop until rabbits exceed 100
while n in range(2,100):
	n=2*n
	generation = generation+1
	print(generation,n)
#print the final sentence
print("after "+str(generation)+" generations,over 100 rabbits have been born.")

