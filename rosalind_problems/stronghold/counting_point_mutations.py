def counting_point_mutations(s,t):
    if len(s)!=len(t):
        raise "not equal length"
    dH=0
    for i in range(len(s)):
        if s[i]!=t[i]:
            dH+=1
    return dH        

fopen = open("./datasets/rosalind_hamm.txt","r")
s = fopen.readline()
t = fopen.readline()
print(counting_point_mutations(s,t))