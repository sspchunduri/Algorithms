# Simple version of GCD
#Recursion method

def recgcd(a,b):
    if(b==0):
        return a
    else:
        return recgcd(b,a%b)

#Eculidean method

def ecugcd(a,b):
    while(b):
        a,b = b,a%b
    return a

#looping
#takes longest time

def loogcd(a,b):
    if a>b:
        s=b
    else:
        s=a
    for i in range(1,s+1):
        if((a%i==0) and (b%i==0)):
            ans = i
        return ans
    