# product of the digit of a given number


n=int(input())
s=0
while(n):
    r=n%10
    s+=r
    n=n//10
print(s)    
