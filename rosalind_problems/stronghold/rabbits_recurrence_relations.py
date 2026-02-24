def fibonacci_rabbits(n, k):
    if n==1 or n==2:
        return 1
    else:
        return k* fibonacci_rabbits(n-2,k) + fibonacci_rabbits(n-1,k)
    
print(fibonacci_rabbits(34,4))  