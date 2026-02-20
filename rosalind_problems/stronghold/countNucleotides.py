def countNucleotidsFrecuency(dna_seq):
    tmpFrecuency = {"A":0,"C":0,"G":0,"T":0}
    for current_nucleotide in dna_seq:
        tmpFrecuency[current_nucleotide] += 1
    return tmpFrecuency


fopen = open("./datasets/rosalinda_dna.txt","r")
DNA_sequence = fopen.read()
result = countNucleotidsFrecuency(DNA_sequence)
print(' '.join([str(value) for key,value in result.items()]))