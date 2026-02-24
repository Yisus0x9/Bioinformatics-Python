def gc_content(sequence):
    count = sequence.count('C') + sequence.count('G')
    return (count / len(sequence)) * 100

def read_fasta(file_path):
    with open(file_path, 'r') as file:
        sequences = {}
        current_id = None
        current_sequence=""
        for line in file:
            print(line)
            if line.startswith('>'):
                if current_sequence!="" and current_id is not None:
                    sequences[current_id]=current_sequence
                    current_sequence=""
                current_id= line.replace('>','').strip()
                print(current_id)
                
            else:
                current_sequence+=line.strip()   
        if current_sequence!="" and current_id is not None:
                    sequences[current_id]=current_sequence
                    current_sequence=""
        return sequences

def get_highest_gc_content():
    highest_gc_id = None
    highest_gc_percentage=0
    sequences= read_fasta("./datasets/rosalinda_gc.txt")
    for seq_id,sequence in sequences.items():
        current_gc_content= gc_content(sequence)
        print(f'{seq_id}: {current_gc_content:.6f}%')
        if current_gc_content >highest_gc_percentage:
            highest_gc_id=seq_id
            highest_gc_percentage=current_gc_content
    return highest_gc_id, highest_gc_percentage        



print(f'{get_highest_gc_content()[0]}\n{get_highest_gc_content()[1]:.6f}')