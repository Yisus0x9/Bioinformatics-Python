DNA_ReverseComplement = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}
def reverse_complement(seq):
    return ''.join(DNA_ReverseComplement[nuc] for nuc in seq)[::-1]

fopen = open("./datasets/rosalind_revc.txt","r")
DNA_sequence = fopen.read()
##DNA_sequence= 'AAAACCCGGT'
result = reverse_complement(DNA_sequence)
print(result)