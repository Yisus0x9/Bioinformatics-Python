def transcribing_dna_into_rna(dna_seq):
    return dna_seq.replace("T","U")


fopen = open("./datasets/rosalinda_rna.txt","r")
DNA_sequence = fopen.read()
result = transcribing_dna_into_rna(DNA_sequence)
print(result)