# DNA Toolkit file
from utilities import *
import collections
Nuecleotids= ['A','T','C','G']
DNA_ReverseComplement = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

#Validate sequemce to make sure it´s a DNA String
def validateSquence(dna_seq):
    upper_dna_seq = dna_seq.upper()
    for current_nucleotide in upper_dna_seq:
        if current_nucleotide not in Nuecleotids:
            return False
    return upper_dna_seq

def countNucleotidsFrecuency(dna_seq):
    tmpFrecuency = {"A":0,"T":0,"C":0,"G":0}
    for current_nucleotide in dna_seq:
        tmpFrecuency[current_nucleotide] += 1
    return tmpFrecuency

def countNucleotidsFrecuencyUsingCollections(dna_seq):
   return dict(collections.Counter(dna_seq))

def transcription(dna_seq):
    return dna_seq.replace("T","U")

def reverse_complement(seq):
    return ''.join(DNA_ReverseComplement[nuc] for nuc in seq)[::-1]

def gc_content(sequence):
    count = sequence.count('C') + sequence.count('G')
    return (count / len(sequence)) * 100

def get_highest_gc_content(sequences):
    highest_gc_id = None
    highest_gc_percentage=0
    for seq_id,sequence in sequences.items():
        current_gc_content= gc_content(sequence)
        print(f'{seq_id}: {current_gc_content:.6f}%')
        if current_gc_content >highest_gc_percentage:
            highest_gc_id=seq_id
            highest_gc_percentage=current_gc_content
    return highest_gc_id, highest_gc_percentage        

def fibonacci_rabbits(n, k):
    if n==1 or n==2:
        return 1
    else:
        return k* fibonacci_rabbits(n-2,k) + fibonacci_rabbits(n-1,k)
    
def translate_rna_protein(sequence):
    slice_index=3
    protein=""
    while slice_index<len(sequence):
        codon=sequence[slice_index-3:slice_index]
        translation=get_aa_by_codon(codon)
        protein+=translation.abrev1
        slice_index+=3
    return protein