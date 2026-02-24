# DNA Toolkit file
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
