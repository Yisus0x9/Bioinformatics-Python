bases=["A","C","G","T"]
def read_fasta(file_path):
    with open(file_path, 'r') as file:
        sequences = []
        current_id = None
        current_sequence=""
        for line in file:
            if line.startswith('>'):
                if current_sequence!="" and current_id is not None:
                    sequences.append(current_sequence)
                    current_sequence=""
                current_id= line.replace('>','').strip()                
            else:
                current_sequence+=line.strip()   
        if current_sequence!="" and current_id is not None:
                    sequences.append(current_sequence)
                    current_sequence=""
        return sequences
def get_profile(matrix):
    profile={}
    for base in bases:
        counts=[]
        for i in range(len(matrix[0])):
            count=0
            for j in range(len(matrix)):
                if(matrix[j][i]==base):
                    count+=1
            counts.append(count)
        profile[base]=counts
    return profile

def get_consensun(profile):
    consensun=""
    profile_temp=list(profile.values())
    for i in range(len(profile_temp[0])):
        max_row_index=0
        max=0
        for j in range(len(profile_temp)):
            if(profile_temp[j][i]>max):
                max_row_index=j
                max=profile_temp[j][i]
        consensun+=bases[max_row_index]
    return consensun
     
FASTA_DATASET="./datasets/rosalind_cons.txt"
matrix=read_fasta(FASTA_DATASET)
profile=get_profile(matrix=matrix)
consensun=get_consensun(profile)
print(consensun)
for key, values in profile.items():
    print(f"{key}: {' '.join(map(str, values))}")
