from dataclasses import dataclass

@dataclass(frozen=True)
class Aminoacido:
    nombre: str
    abrev3: str
    abrev1: str

GENETIC_CODE = {
    # Fenilalanina
    "UUU": Aminoacido("Fenilalanina", "Phe", "F"),
    "UUC": Aminoacido("Fenilalanina", "Phe", "F"),
    # Leucina
    "UUA": Aminoacido("Leucina", "Leu", "L"),
    "UUG": Aminoacido("Leucina", "Leu", "L"),
    "CUU": Aminoacido("Leucina", "Leu", "L"),
    "CUC": Aminoacido("Leucina", "Leu", "L"),
    "CUA": Aminoacido("Leucina", "Leu", "L"),
    "CUG": Aminoacido("Leucina", "Leu", "L"),
    # Isoleucina
    "AUU": Aminoacido("Isoleucina", "Ile", "I"),
    "AUC": Aminoacido("Isoleucina", "Ile", "I"),
    "AUA": Aminoacido("Isoleucina", "Ile", "I"),
    # Metionina (inicio)
    "AUG": Aminoacido("Metionina", "Met", "M"),
    # Valina
    "GUU": Aminoacido("Valina", "Val", "V"),
    "GUC": Aminoacido("Valina", "Val", "V"),
    "GUA": Aminoacido("Valina", "Val", "V"),
    "GUG": Aminoacido("Valina", "Val", "V"),
    # Serina
    "UCU": Aminoacido("Serina", "Ser", "S"),
    "UCC": Aminoacido("Serina", "Ser", "S"),
    "UCA": Aminoacido("Serina", "Ser", "S"),
    "UCG": Aminoacido("Serina", "Ser", "S"),
    "AGU": Aminoacido("Serina", "Ser", "S"),
    "AGC": Aminoacido("Serina", "Ser", "S"),
    # Prolina
    "CCU": Aminoacido("Prolina", "Pro", "P"),
    "CCC": Aminoacido("Prolina", "Pro", "P"),
    "CCA": Aminoacido("Prolina", "Pro", "P"),
    "CCG": Aminoacido("Prolina", "Pro", "P"),
    # Treonina
    "ACU": Aminoacido("Treonina", "Thr", "T"),
    "ACC": Aminoacido("Treonina", "Thr", "T"),
    "ACA": Aminoacido("Treonina", "Thr", "T"),
    "ACG": Aminoacido("Treonina", "Thr", "T"),
    # Alanina
    "GCU": Aminoacido("Alanina", "Ala", "A"),
    "GCC": Aminoacido("Alanina", "Ala", "A"),
    "GCA": Aminoacido("Alanina", "Ala", "A"),
    "GCG": Aminoacido("Alanina", "Ala", "A"),
    # Tirosina
    "UAU": Aminoacido("Tirosina", "Tyr", "Y"),
    "UAC": Aminoacido("Tirosina", "Tyr", "Y"),
    # Stop
    "UAA": Aminoacido("Stop", "Stop", "*"),
    "UAG": Aminoacido("Stop", "Stop", "*"),
    "UGA": Aminoacido("Stop", "Stop", "*"),
    # Histidina
    "CAU": Aminoacido("Histidina", "His", "H"),
    "CAC": Aminoacido("Histidina", "His", "H"),
    # Glutamina
    "CAA": Aminoacido("Glutamina", "Gln", "Q"),
    "CAG": Aminoacido("Glutamina", "Gln", "Q"),
    # Asparagina
    "AAU": Aminoacido("Asparagina", "Asn", "N"),
    "AAC": Aminoacido("Asparagina", "Asn", "N"),
    # Lisina
    "AAA": Aminoacido("Lisina", "Lys", "K"),
    "AAG": Aminoacido("Lisina", "Lys", "K"),
    # Ácido aspártico
    "GAU": Aminoacido("Ácido aspártico", "Asp", "D"),
    "GAC": Aminoacido("Ácido aspártico", "Asp", "D"),
    # Ácido glutámico
    "GAA": Aminoacido("Ácido glutámico", "Glu", "E"),
    "GAG": Aminoacido("Ácido glutámico", "Glu", "E"),
    # Cisteína
    "UGU": Aminoacido("Cisteína", "Cys", "C"),
    "UGC": Aminoacido("Cisteína", "Cys", "C"),
    # Triptófano
    "UGG": Aminoacido("Triptófano", "Trp", "W"),
    # Arginina
    "CGU": Aminoacido("Arginina", "Arg", "R"),
    "CGC": Aminoacido("Arginina", "Arg", "R"),
    "CGA": Aminoacido("Arginina", "Arg", "R"),
    "CGG": Aminoacido("Arginina", "Arg", "R"),
    "AGA": Aminoacido("Arginina", "Arg", "R"),
    "AGG": Aminoacido("Arginina", "Arg", "R"),
    # Glicina
    "GGU": Aminoacido("Glicina", "Gly", "G"),
    "GGC": Aminoacido("Glicina", "Gly", "G"),
    "GGA": Aminoacido("Glicina", "Gly", "G"),
    "GGG": Aminoacido("Glicina", "Gly", "G"),
}

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