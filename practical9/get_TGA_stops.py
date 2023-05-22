# read the file, identify sequences which end with the ‘TGA’ stop codon
# and simplify the sequence name by only putting the gene name.
# Output the results in a new fasta file TGA_genes.fa.
# Note that the sequences for each gene run onto several lines.



# read the file
input=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')

# Output the results in a new fasta file TGA_genes.fa.
output=open('TGA_gene.fa','w')

# use re function to match
import re

# initialize the variables
current_gene = ''
current_sequence = ''

# go through all the lines
for line in input:
     if line.startswith('>'):  # to find the gene name lines
        line = line.strip()  # to strip the n/ at the end of lines
   
        if current_gene != '' and current_sequence.endswith('TGA'):  # there's a gene, and the stop codon is TGA
            output.write(f'>{current_gene}\n{current_sequence}\n')  # write in the gene name and sequence

        # get the gene name
        gene_match = re.match(r'>.*gene:(\w+).*', line)
        if gene_match:
            current_gene = gene_match.group(1)
        else:
            current_gene = ''
        current_sequence = ''  # reinitialize the current sequence
     else:  
        current_sequence += line  # append the gene sequence
# close the file
input.close()
output.close()

with open('TGA_gene.fa', 'r') as file:
    for i in range(5):
        line = file.readline()
        print(line)

##there's just empty results!

# I don't know what's wrong with it!
# I thought I did my best.
# I'm sorry.


