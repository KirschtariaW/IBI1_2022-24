#1. Asks the user to input one of the three stop codons (TAA’, ‘TAG’ or ‘TGA’) which should be used to create a filename as the new fasta file to be written to, e.g. if the given stop codon is ‘TAA’ the output file should be ‘TAA_stop_genes.fa’;
#2. Stores the sequences of genes whose sequences end with the given stop codon in fasta format (do not put line breaks in the sequence as in the original file, so that the entire sequence is on one line);
#3. The sequence name of each gene contains only the gene name, and the number of coding sequences which could be generated using the given stop codon.

# use regular expression
import re

codon = input('Stop codon: ') #IDE do not support cosole input. 
#codon= 'TAG'  # that's what I used for test running 

#format: to put codon into {}
# use regular expression to find the lines that can fit in
pattern = re.compile(r'>(\S+).*{}.*'.format(codon))


with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') as input, \
     open('{}_stop_genes.fa'.format(codon), 'w') as output:
    gene_data = input.read()
    matches = pattern.findall(gene_data) # to find all the genes having this pattern and store them in matches
   # match: strings that from matches. they are the strings that fit in the pattern. i.e. the gene names
    for match in matches:
        output.write('>{}\n\n'.format(match))

input.close()
output.close()

# one of my classmates taught me that
# but the results are just some repeated numbers, not the file
# I can't understand 
# sorry
