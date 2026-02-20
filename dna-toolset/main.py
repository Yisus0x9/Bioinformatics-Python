# DNA Toolset testing file
from DNAToolkit import *
import random


## Generate a valid random DNA sequence
random_dna_seq = ''.join([random.choice(Nuecleotids) for nuc in range (30)])

DNA_sequence=validateSquence(random_dna_seq)
fopen = open("./dna-toolset/rosalinda_dna.txt","r")
DNA_sequence = fopen.read()
DNA_sequence=validateSquence(random_dna_seq)
print(countNucleotidsFrecuencyUsingCollections(DNA_sequence))