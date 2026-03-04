from utils import read_fasta

def shared_substrings(sequences):
    substrings=set()
    rechazadas = set()  # ← Guardamos las que no pasaron
    limit=len(sequences[0])
    print(limit)
    print(len(sequences))
    jump=2
    while jump<=limit:
        i=0
        while i+jump <= limit:
            print(i+jump)
            all_exists=True
            search_seq=sequences[0][i:i+jump]
            if(not search_seq in substrings and search_seq not in rechazadas):
                for seq in sequences:
                    if(not (search_seq in seq)):
                        all_exists=False
                        break
                if(all_exists):
                    #print(f' secuencia encontrada {search_seq}')
                    substrings.add(search_seq)
                else:
                    rechazadas.add(search_seq)
            i+=1     
        jump+=1
    return substrings

dataset_path="./datasets/rosalind_lcsm.txt"
records=read_fasta(dataset_path)
sequences=list(records.values())
file=open("./outputs/sequences.txt","w+")
for s in sequences:
    file.write(f'{str(s)}\n')
file.close()
file=open("./outputs/rosalind_lcsm.txt","w+")
shared=list(shared_substrings(sequences))
shared.sort(key=len)
for s in shared:
    file.write(f'{str(s)}\n')
file.close()
