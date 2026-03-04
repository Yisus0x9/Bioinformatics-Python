from utils import GENETIC_CODE

def get_aa_by_codon(codon):
     return GENETIC_CODE.get(codon)

def translate_rna_protein(sequence):
    slice_index=3
    protein=""
    while slice_index<len(sequence):
        codon=sequence[slice_index-3:slice_index]
        translation=get_aa_by_codon(codon)
        protein+=translation.abrev1
        slice_index+=3
    return protein

fopen = open("./datasets/rosalind_prot.txt","r")
RNA_sequence = fopen.read()
print(translate_rna_protein(RNA_sequence))