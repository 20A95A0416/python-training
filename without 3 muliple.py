n=int(input())
for i in range(1,21):
    if(i%3==0):
        continue
    print(n,'x',i,'=',n*i)
