# DNA Toolset testing file
from DNAToolkit import *
from utilities import colored
import random


## Generate a valid random DNA sequence
random_dna_seq = ''.join([random.choice(Nuecleotids) for nuc in range (30)])

DNA_sequence=validateSquence(random_dna_seq)
print(f'\n Sequence: {colored(DNA_sequence)}')
print(f'[1] + Sequence length: {len(DNA_sequence)}')
print(colored(f'[2] + Nucleotids Frecuency: {countNucleotidsFrecuency(DNA_sequence)}'))
print(f'[3] + DNA/RNA Transcription: {colored(transcription(DNA_sequence))}')
print(f"[4] + Reverse Complement:\n5' {colored(DNA_sequence)} 3'")
print(f"   {''.join(['|' for nuc in range(len(DNA_sequence))])}")
print(f"3' {colored(reverse_complement(DNA_sequence))} 5'")
print(countNucleotidsFrecuencyUsingCollections(DNA_sequence))
