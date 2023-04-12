#count the total number of possible coding sequences formed by this sequence

#create the sequence
seq='ATGCAATCGACTACGATCTGAGAGGGCCTAA'

#use the regular expression
import re
#find all the string starting with ATG, ending with ‘TAA’, ‘TAG’, or ‘TGA’.
a=re.findall(r'ATG.*TAA',seq)
b=re.findall(r'ATG.*TAG',seq)
c=re.findall(r'ATG.*TGA',seq)
#count the number of all the strings
count=len(a)+len(b)+len(c)
print(count)
