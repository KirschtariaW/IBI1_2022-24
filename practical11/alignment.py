# In the simplest form, sequence comparison is just a string comparison. 
# However, additional considerations such as the frequency of individual amino acid substitutions add some complexity to the task.

# we use BLOSUM (BLOcks SUbstitution Matrix) matrix for protein alignment
# BLOSUM is a substitution matrix which can be used to quantify alignments between evolutionarily divergent proteins.
# The original matrix was obtained by analysis of highly conserved regions in a number of protein families. 
#The relative frequencies of amino acids and their substitution probabilities 
#were used to calculate a log-odds score1 for each of the possible substitution pairs of the 20 standard amino acids.

# all the BLOSUM matrixes are based on observed alignments
# The number after BLOSUM indicates the criteria used to build the matrix. 
#For example, BLOSUM62 is the matrix built using sequences with less than 62% similarity (sequences with ≥ 62% identity were clustered).
# It is the default setting as benchmarking of BLOSUM matrixes has identified that BLOSUM62 is among the best for detecting weak sequence similarities.

# implement a simple pairwise non-gapped global alignment2 and use that for comparing the protein sequences 
#pairwise non-gapped global alignment
# What this means is that we compare two sequences (pairwise) without considering the possibility for amino acid insertions or deletions (non-gapped).
# We perform a global (instead of a local) alignment starting from amino acid 1 and ending with the last amino acid.
#  print out the analyzed sequences in addition to the final BLOSUM score.
# You should also print out the percentage identity (how many amino acids are identical).

# reference1: 传统蛋白质序列比对算法 - 王思若的文章 - 知乎 https://zhuanlan.zhihu.com/p/437654967
# reference2: https://blog.csdn.net/laixiangwei/article/details/105831376
# BLOSUM62 also come from: https://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt


####1. input files
#read the sequence1 and 2
#read BLOSUM62 matrix

####2.compare each amino acid
# for i in length ...
# find score and add it to a new vector
# sum scores

####3. print output
# print edit distance


####1.input files
# read the sequences

with open('ACE2_cat.fa') as file:
    file_content = file.read()

# get amino acid sequence
amino_sequence = ''
lines = file_content.split('\n')
for line in lines:
    if line.startswith('>'):
        continue
    amino_sequence += line.strip()

cat= amino_sequence

with open('ACE2_human.fa') as file:
    file_content = file.read()
amino_sequence = ''
lines = file_content.split('\n')
for line in lines:
    if line.startswith('>'):
        continue
    amino_sequence += line.strip()

human= amino_sequence


class alignment:
    def __init__(self, sequence1, sequence2):
        self.sequence1 = sequence1
        self.sequence2 = sequence2
    
    def pairwise_alignment(self): #read BLOSUM62 matrix
        amino_acid=['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X', '*']
        BLOSUM62 = [[ 4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -1, -1, -2, -1,  1,  0, -3, -2,  0, -2, -1,  0, -4],
                    [-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -1, -3, -2, -1, -1, -3, -2, -3, -1,  0, -1, -4],
                    [-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3,  3,  0, -1, -4],
                    [-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3,  4,  1, -1, -4],
                    [ 0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2, -4],
                    [-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2,  0,  3, -1, -4],
                    [-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
                    [ 0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3, -1, -2, -1, -4],
                    [-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3,  0,  0, -1, -4],
                    [-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3, -3, -3, -1, -4],
                    [-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1, -4, -3, -1, -4],
                    [-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2,  0,  1, -1, -4],
                    [-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1, -3, -1, -1, -4],
                    [-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1, -3, -3, -1, -4],
                    [-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2, -2, -1, -2, -4],
                    [ 1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2,  0,  0,  0, -4],
                    [ 0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5, -2, -2,  0, -1, -1,  0, -4],
                    [-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3, -4, -3, -2, -4],
                    [-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1, -3, -2, -1, -4],
                    [ 0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4, -3, -2, -1, -4],
                    [-2, -1,  3,  4, -3,  0,  1, -1,  0, -3, -4,  0, -3, -3, -2,  0, -1, -4, -3, -3,  4,  1, -1, -4],
                    [-1,  0,  0,  1, -3,  3,  4, -2,  0, -3, -3,  1, -1, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
                    [ 0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2,  0,  0, -2, -1, -1, -1, -1, -1, -4],
                    [-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,  1],
                    ]
 
   


# below was what I tried to write originally after the BLOSUM
# only with a dictionary BLOSUM62, it might work 
# but it was so hard to turn the BLOSUM62 matrix into a dictionary
# and different from the reference


edit_distance=0 #set initial distance as 0
    for i in range (len(self.sequence1)):#compair each amino acid
        if self.sequence1[i] != self.sequence2[i]:
            edit_distance+= BLOSUM62[(self.sequence1[i],self.sequence2[i])] #add a score 1 if amino acids are different

        print(edit_distance)


# failed

#example 
a=alignment(cat,human)
a.pairwise_alignment()



