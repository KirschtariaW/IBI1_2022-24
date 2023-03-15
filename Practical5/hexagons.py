#calculate the hexagon sequences and display first 5 values
#write a loop showing the accumulation of sequences
#start from 1 point
n=1
h=1
print(n,h)
#h= n*(2n-1)
for n in range(1,5):
	n=n+1
	h=n*(2*n-1)
#print:n,h
	print(n,h)

