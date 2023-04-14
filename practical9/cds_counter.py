#count the total number of possible coding sequences formed by this sequence

#create the sequence
seq='ATGCAATCGACTACGATCTGAGAGGGCCTAA'

#for re.findall can just find one longest sequence, so it is not good in this task

#the true way to do so
#use if 
if seq.count('ATG')== 0: #find ATG exist
    print("no sequence")
elif seq.count('ATG')>= 1:
    count=seq.count('TGA')+seq.count('TAG')+seq.count('TAA') #find the number of each end codon
    print(count)
