#for loop


n=int(input())
for i in range(1,13):
    if(n*i>35):
        break
    print(n,'x',i,'=',n*i)
