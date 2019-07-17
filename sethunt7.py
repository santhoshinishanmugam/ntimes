s=int(input())
d=list(map(int,input().split()))
for i in range(len(d)):
  if((i%d==0)and(d[i]%2!=0)or(i%2!=0)and(d[i]%==0)):
    print(d[i],end=" ")
