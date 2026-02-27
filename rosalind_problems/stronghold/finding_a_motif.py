def finding_substring(s,t):
    finds=[]
    lenght=len(t)
    for i in range(len(s)):
        if(i+lenght<len(s)):
            if(s[i]==t[0] and s[i:i+lenght]==t):
                finds.append(i+1)
                print(f'index: {i+1} : {s[i:i+lenght]} : init {s[i]}')
    return finds

fopen = open("./datasets/rosalind_subs.txt","r")
DNA_seq=fopen.readline().strip()
t=fopen.readline().strip()
result=finding_substring(DNA_seq,t)
print(f'{str(result).replace(",","").replace("[","").replace("]","").strip()}')

