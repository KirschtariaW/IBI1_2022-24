#  a function that determines whether a given DNA sequence is likely to be protein-coding or not. 
# calculate the distance in a DNA string between an opening ‘ATG’ codon and a final stop ‘TGA’ codon.

#  a sequence where more than 50% of the total DNA is within these codons is protein-coding; 
# a sequence where less than 10% of the total DNA is within these codons is non-coding
# everything else is unclear

# assume that there is exactly one ‘ATG’ start 
# and one ‘TGA’ stop codon in the given sequence.

#  take as input a single string variable describing a DNA sequence
# return the percentage of this sequence which is coding 
# and whether the sequence should be labelled as ‘protein-coding’, ‘non-coding’, or ‘unclear’
   

#use regular expression
import re

class ProteinClass:
    def __init__(self, sequence):
        self.sequence = sequence
        self.coding = re.search(r'.*ATG.*TGA.*', sequence)# find the coding region
        self.percentage = len(self.coding.group()) / len(sequence) * 100# use group() to return the string of coding region

    def define(self):
        base = ["A", "T", "G", "C"]#to know whether it is a DNA sequence
        if not isinstance(self.sequence, str):
            return "The input can only be a string"
        else:
            for character in self.sequence:
                if character not in base:
                    return "The input is not a DNA sequence"
        
        if re.search('ATG', self.sequence) and re.search('TGA', self.sequence):#to find there's ATG and TGA in the sequence, and their precentage
            if self.percentage > 50:
                return (f"protein-coding, {self.percentage}%")
            elif self.percentage < 10:
                return (f"non-coding, {self.percentage}%")
            else:
                return (f"unclear ,{self.percentage}%")
        else:
            return "no ATG or GTA, not a full sequence"

#example
sequence = "ATGAAAAAAAAAATGA"
protein = ProteinClass(sequence)
protein.define()


